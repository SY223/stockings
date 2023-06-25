from rest_framework import serializers
from stockright.models import Pond, StockingDensity
from django.contrib.auth.models import User
from stockright.pond_logic import pondvolume, thirty_p_decrease, twenty_p_decrease



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PondSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(source='date_added', read_only=True)
    owner = UserSerializer(read_only=True)
    #owner = serializers.StringRelatedField()
    class Meta:
        model = Pond
        fields = ['id', 'name', 'created_date','owner']
        read_only_fields = ['created_date']
    


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

