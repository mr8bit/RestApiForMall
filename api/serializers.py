from rest_framework import serializers
from advertising.models import *
from shop_and_sales.models import *
from terminals.models import *
from django.db import models
from RestApiForMall import settings


class AdvertisingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advertising
        fields = ('file', 'duration')


class PlayListAdvertisingSerializer(serializers.ModelSerializer):
    ads = AdvertisingSerializer(many=True, read_only=True)

    class Meta:
        model = PlayListAdvertising
        fields = ('name', 'ads')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ShopSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='category.name', read_only=True, many=False)

    class Meta:
        model = Shop
        fields = ('name', 'description', 'logo', 'photo', 'category', 'mapID', 'mapLogo')


class TerminalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terminal
        fields = ('name', 'position')


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = ('image',)
