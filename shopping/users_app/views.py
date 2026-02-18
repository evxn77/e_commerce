from django.shortcuts import render, redirect, get_object_or_404
from main_app.models import Product, Order
from django.contrib.auth.decorators import login_required

@login_required
def place_order(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        # Create the order
        Order.objects.create(
            user=request.user,
            product=product,
            status='Pending'
        )
        return redirect('my_orders')

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-date_ordered')

    return render(request, 'users_app/my_orders.html', {'orders': orders})
