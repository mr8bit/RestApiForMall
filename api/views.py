from rest_framework import routers, serializers, viewsets, generics
from django.shortcuts import render
from advertising.models import *
from shop_and_sales.models import *
from terminals.models import *
from .serializers import *
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class PlayListAdvertisingViewSet(viewsets.ModelViewSet):
    serializer_class = PlayListAdvertisingSerializer
    queryset = PlayListAdvertising.objects.all()

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'advertisement': serializer.data})


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'shops': serializer.data})


class TerminalViewSet(viewsets.ModelViewSet):
    serializer_class = TerminalSerializer
    queryset = Terminal.objects.all()

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'terminals': serializer.data})

class SalesViewSet(viewsets.ModelViewSet):
        serializer_class = SalesSerializer
        queryset = Sale.objects.all()

        def list(self, request, *args, **kwargs):
            self.object_list = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(self.object_list, many=True)
            return Response({'sales': serializer.data})