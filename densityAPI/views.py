from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import permissions, status
from stockright.models import Pond, StockingDensity
from .serializers import PondSerializer, DensitySerializer, UserSerializer
from stockright.pond_logic import pondvolume, thirty_p_decrease, twenty_p_decrease
from django.core.paginator import Paginator, EmptyPage
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


@api_view(['GET', 'POST'])
def pond_list_create(request):
    if request.method == 'GET':
        ponds = Pond.objects.filter(owner=request.user).order_by('-date_added')
        search = request.query_params.get('search') #to search
        if search:
            ponds = ponds.filter(name__icontains=search)
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)
        paginator = Paginator(ponds, per_page=perpage)
        try:
            ponds = paginator.page(number=page)
        except EmptyPage:
            ponds = []
        serializeed_item = PondSerializer(ponds, many=True)
        return Response(serializeed_item.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serialized_item = PondSerializer(data=request.data)
        if serialized_item.is_valid():
            serialized_item.save(owner=request.user)
            return Response(serialized_item.data, status=status.HTTP_201_CREATED)
        return Response(serialized_item.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def pond_detail(request, pondId):
    try:
        pond = Pond.objects.get(id=pondId, owner=request.user)
    except Pond.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialized_item = PondSerializer(pond)
        return Response(serialized_item.data)
    elif request.method == 'PUT':
        serialized_item = PondSerializer(pond, data=request.data)
        if serialized_item.is_valid():
            serialized_item.save()
            return Response(serialized_item.data)
        return Response(serialized_item.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pond.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def densities_list_create(request, pondId):
    if request.method == 'GET':
        pond = Pond.objects.get(id=pondId)
        single_pond_densities = pond.stockingdensity_set.order_by('-date_checked')
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)
        paginator = Paginator(single_pond_densities, per_page=perpage)
        try:
            single_pond_densities = paginator.page(number=page)
        except EmptyPage:
            single_pond_densities = []
        serialized_item = DensitySerializer(single_pond_densities, many=True)
        return Response(serialized_item.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        pond= Pond.objects.get(id=pondId)
        serialized_item = DensitySerializer(data=request.data)
        if serialized_item.is_valid():
            validated_data = serialized_item.validated_data
            validated_data['pond'] = pond
            validated_data['to_stock'] = pondvolume(validated_data['length'], validated_data['width'], validated_data['height'])
            validated_data['verdict'] = str(validated_data['to_stock'])
            validated_data['thirty_percent_decrease'] = thirty_p_decrease(validated_data['to_stock'])
            validated_data['twenty_percent_decrease'] = twenty_p_decrease(validated_data['to_stock'])
            instance = StockingDensity(**validated_data)
            instance.save()
            return Response(serialized_item.data, status=status.HTTP_201_CREATED)
        return Response(serialized_item.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def density_detail(request, densityId):
    try:
        density = StockingDensity.objects.get(id=densityId)
    except StockingDensity.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialized_item = DensitySerializer(density)
        return Response(serialized_item.data)
    elif request.method == 'PUT':
        serialized_item = DensitySerializer(density, data=request.data)
        if serialized_item.is_valid():
            serialized_item.save()
            return Response(serialized_item.data)
        return Response(serialized_item.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        density.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def user_list_create(request):
    if request.user.groups.filter(name='Manager').exists():
        if request.method == 'GET':
            queryset = User.objects.all()
            serialized_item = UserSerializer(queryset, many=True)
            return Response(serialized_item.data, status=status.HTTP_200_OK)
        if request.method == 'POST':
            serialized_item = UserSerializer(data=request.data)
            if serialized_item.is_valid():
                serialized_item.save()
                return Response(serialized_item.data, status=status.HTTP_201_CREATED)
            return Response(serialized_item.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"Error": "Only the admin manager is authorised to view this page."})


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    if request.user.groups.filter(name='Manager').exists():
        try:
            queryset = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'GET':
            serialized_item = UserSerializer(queryset)
            return Response(serialized_item.data)
        elif request.method == 'PUT':
            serialized_item = UserSerializer(data=request.data)
            if serialized_item.is_valid():
                serialized_item.save()
                return Response(serialized_item.data)
            return Response(serialized_item.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            queryset.delete()
            return Response(status=status.HTTP_200_OK)
    else:
        return Response({"Error": "Only the admin manager is authorised to view this page."})





