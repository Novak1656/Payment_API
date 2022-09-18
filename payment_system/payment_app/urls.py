from django.urls import path
from .views import ItemAPIView, BuyItemAPIView, success

urlpatterns = [
    path('buy/<int:pk>', BuyItemAPIView.as_view(), name='buy_item'),
    path('item/<int:pk>', ItemAPIView.as_view(), name='get_item'),
    path('success', success, name='success')
]
