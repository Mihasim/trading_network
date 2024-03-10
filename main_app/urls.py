from django.urls import path

from main_app.apps import MainAppConfig

from main_app.views import TheLinkOfTheNetworkCreateAPIView, TheLinkOfTheNetworkListAPIView, \
    TheLinkOfTheNetworkRetrieveAPIView, TheLinkOfTheNetworkUpdateAPIView, TheLinkOfTheNetworkDestroyAPIView, \
    ProductCreateAPIView, ProductListAPIView, ProductRetrieveAPIView, ProductUpdateAPIView, ProductDestroyAPIView

app_name = MainAppConfig.name

urlpatterns = [
    # Звенья сети
    path('link_net/create/', TheLinkOfTheNetworkCreateAPIView.as_view(), name='link_of_network-create'),
    path('link_nets/', TheLinkOfTheNetworkListAPIView.as_view(), name='links_of_networks-list'),
    path('link_net/<int:pk>/', TheLinkOfTheNetworkRetrieveAPIView.as_view(), name='get-link_of_network'),
    path('link_net/update/<int:pk>/', TheLinkOfTheNetworkUpdateAPIView.as_view(), name='link_of_network-update'),
    path('link_net/delete/<int:pk>/', TheLinkOfTheNetworkDestroyAPIView.as_view(), name='link_of_network-delete'),

    # продукты
    path('product/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('products/', ProductListAPIView.as_view(), name='products-list'),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='get-product'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('product/delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product-delete'),
]
