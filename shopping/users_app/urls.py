from django.urls import path
from . import views

urlpatterns = [
    path('place-order/<int:product_id>/', views.place_order, name='place_order'),
    path('my-orders/', views.my_orders, name='my_orders'),
]