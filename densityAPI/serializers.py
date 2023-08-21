from rest_framework import serializers
from stockright.models import Pond, StockingDensity, CustomUser
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token
from dj_rest_auth.serializers import LoginSerializer
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model





class CustomLoginSerializer(LoginSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username', None)
    class Meta:
        pass


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'email_address_verified', 'is_active', 'date_joined']



class PondSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    created_date = serializers.DateTimeField(source='date_added', read_only=True)
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Pond
        fields = ['id', 'name', 'created_date','owner']
        read_only_fields = ['created_date']

    def validate_name(self, value):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            user=request.user
            if Pond.objects.filter(name__icontains=value, owner=user).exists():
                raise serializers.ValidationError({'error': 'name already in use..'})
        return value

        

class DensitySerializer(serializers.ModelSerializer):
    pond = PondSerializer(read_only=True)
    to_stock = serializers.FloatField(read_only=True)
    verdict = serializers.CharField(read_only=True)
    twenty_percent_decrease = serializers.FloatField(read_only=True)
    thirty_percent_decrease = serializers.FloatField(read_only=True)
    class Meta:
        model = StockingDensity
        fields = [
            'id', 'pond', 'length', 'width', 'height', 'to_stock', 'verdict', 'twenty_percent_decrease', \
                'thirty_percent_decrease', 'date_checked'         
        ]

