from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Item, Order
import stripe
from django.conf import settings


def get_item(item_pk):
    return get_object_or_404(Item, pk=item_pk)


class ItemAPIView(APIView):
    def get(self, request, **kwargs):
        api_key = settings.STRIPE_PUBLIC_KEY
        return render(request, 'payment_app/item_page.html', {'item': get_item(kwargs.get('pk')), 'api_key': api_key})


class BuyItemAPIView(APIView):
    def get(self, request, **kwargs):
        item = get_item(kwargs.get('pk'))
        stripe.api_key = settings.STRIPE_SECRET_KEY
        domain = 'http://127.0.0.1:8000'
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f'{domain}/success',
            cancel_url=f"{domain}{reverse('get_item', kwargs={'pk': kwargs.get('pk')})}",
        )
        return JsonResponse({'session_id': session.id})


def success(request):
    return render(request, 'payment_app/success.html')


# Views для бонусных заданий
def get_order(order_pk):
    return Order.objects.filter(pk=order_pk).select_related('discount').prefetch_related('items').first()


class OrderAPIView(APIView):
    def get(self, request, **kwargs):
        order = get_order(kwargs.get('order_pk'))
        items = order.items.all()
        unit_amount = items.aggregate(unit_amount=Sum('price'))['unit_amount']
        api_key = settings.STRIPE_PUBLIC_KEY
        context = {'order': order, 'items': items, 'api_key': api_key, 'unit_amount': unit_amount}
        return render(request, 'payment_app/order_page.html', context)


class BuyOrderAPIView(APIView):
    def get(self, request, **kwargs):
        order = get_order(kwargs.get('order_pk'))
        items = order.items.all()
        stripe.api_key = settings.STRIPE_SECRET_KEY
        discounts = []
        if order.discount:
            coupon = stripe.Coupon.create(percent_off=order.discount.discount_value)
            discounts = [{'coupon': f'{coupon.id}', }]
        domain = 'http://127.0.0.1:8000'
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': item.price,
                    },
                'quantity': 1,
                }for item in items],
            mode='payment',
            discounts=discounts,
            success_url=f'{domain}/success',
            cancel_url=f"{domain}{reverse('buy_order', kwargs={'order_pk': kwargs.get('order_pk')})}",
        )
        return JsonResponse({'session_id': session.id})
