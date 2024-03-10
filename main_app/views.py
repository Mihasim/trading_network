from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import generics

from main_app.models import TheLinkOfTheNetwork, Product
from main_app.permissions import IsActiveStaff
from main_app.serializers import ProductSerializer, TheLinkOfTheNetworkSerializer


# Контроллеры звеньев сети продаж
class TheLinkOfTheNetworkCreateAPIView(generics.CreateAPIView):
    serializer_class = TheLinkOfTheNetworkSerializer


class TheLinkOfTheNetworkListAPIView(generics.ListAPIView):
    serializer_class = TheLinkOfTheNetworkSerializer
    queryset = TheLinkOfTheNetwork.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['country',]
    ordering_fields = ['country',]
    permission_classes = [IsActiveStaff]


class TheLinkOfTheNetworkRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = TheLinkOfTheNetworkSerializer
    queryset = TheLinkOfTheNetwork.objects.all()
    permission_classes = [IsActiveStaff]


class TheLinkOfTheNetworkUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TheLinkOfTheNetworkSerializer
    queryset = TheLinkOfTheNetwork.objects.all()
    permission_classes = [IsActiveStaff]


class TheLinkOfTheNetworkDestroyAPIView(generics.DestroyAPIView):
    queryset = TheLinkOfTheNetwork.objects.all()
    permission_classes = [IsActiveStaff]


# Контроллеры продуктов
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsActiveStaff]


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveStaff]


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveStaff]


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveStaff]


class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsActiveStaff]
