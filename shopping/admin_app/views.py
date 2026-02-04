from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from main_app.models import Product, Order
from django.db.models import Sum
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ProductForm
from django.contrib import messages

@staff_member_required
def admin_dashboard(request):
    # Total Users
    total_users = User.objects.count()
    # Total Products
    total_products = Product.objects.count()
    # Total Orders
    total_orders = Order.objects.count()
    # Total Revenue (Sum of prices of all ordered products)
    total_revenue = Order.objects.aggregate(total=Sum('product__price'))['total'] or 0
    
    context = {
        'total_users': total_users,
        'total_products': total_products,
        'total_orders': total_orders,
        'total_revenue': total_revenue, # Pass this to dashboard too!
    }
    return render(request, 'admin_app/dashboard.html', context)

@staff_member_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added.")
            return redirect('add_product')
    else:
        form = ProductForm()
    return render(request, 'admin_app/add_product.html', {'form': form})

@staff_member_required
def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('collections')
    else:
        form = ProductForm(instance=product)
    return render(request, 'admin_app/add_product.html', {'form': form, 'edit_mode': True})

@staff_member_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('collections')
    return render(request, 'admin_app/delete_confirm.html', {'product': product})

@staff_member_required
def sale_report(request):
    total_rev = Order.objects.aggregate(total=Sum('product__price'))['total'] or 0
    context = {
        'total_revenue': total_rev,
        'recent_orders': Order.objects.all().order_by('-date_ordered')
    }
    return render(request, 'admin_app/sale_report.html', context)

@staff_member_required
def view_all_users(request):
    users = User.objects.all()
    return render(request, 'admin_app/view_users.html', {'users': users})