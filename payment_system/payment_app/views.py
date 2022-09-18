from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import Item
import stripe
from django.conf import settings


def success(request):
    return render(request, 'payment_app/success.html')


class ItemAPIView(APIView):
    def get(self, request, **kwargs):
        item = get_object_or_404(Item, pk=kwargs.get('pk'))
        api_key = settings.STRIPE_PUBLIC_KEY
        return render(request, 'payment_app/item_page.html', {'item': item, 'api_key': api_key})


class BuyItemAPIView(APIView):
    def get(self, request, **kwargs):
        item = get_object_or_404(Item, pk=kwargs.get('pk'))
        stripe.api_key = settings.STRIPE_SECRET_KEY
        domain = 'http://127.0.0.1:8000'
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f'{item.name}',
                    },
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f'{domain}/success',
            cancel_url=request.META["HTTP_REFERER"],
        )
        return JsonResponse({'session_id': session.id})
