from django.urls import path
from .views import ItemAPIView, BuyItemAPIView, success, OrderAPIView, BuyOrderAPIView

urlpatterns = [
    path('buy/item/<int:pk>', BuyItemAPIView.as_view(), name='buy_item'),
    path('item/<int:pk>', ItemAPIView.as_view(), name='get_item'),

    # Urls для бонусных заданий
    path('order/<int:order_pk>', OrderAPIView.as_view(), name='get_order'),
    path('buy/order/<int:order_pk>', BuyOrderAPIView.as_view(), name='buy_order'),

    path('success', success, name='success')
]
