from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Order

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            passcode = request.POST.get('admin_passcode')

            if user.is_staff:
                if passcode == "0000":
                    login(request, user)
                    messages.success(request, "Master Access Granted.")
                    return redirect('admin_dashboard')
                else:
                    messages.error(request, "Invalid Admin Passcode.")
                    return render(request, 'main_app/login.html', {'form': form})
            
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main_app/login.html', {'form': form})

def collections_view(request):
    products = Product.objects.all()
    return render(request, 'main_app/collections.html', {'products': products})

@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Order.objects.create(user=request.user, product=product, status='pending')
    messages.success(request, f"Added {product.name} to your cart.")
    return redirect('collections')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        admin_code = request.POST.get('admin_registration_code')

        if form.is_valid():
            # Save the user 
            user = form.save()
            
            # Admin Switch
            if admin_code == "0000":
                user.is_staff = True
                user.is_superuser = True
                user.save()
                messages.success(request, "Admin account initialized. Access granted.")
            else:
                messages.success(request, "Account created! Welcome to ShopEasy.")

            # Log the user in automatically
            login(request, user)
            
            # Redirect to Home page
            return redirect('home')
        else:
            # If form is invalid 
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = UserCreationForm()
        
    return render(request, 'main_app/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def home_view(request):
    return render(request, 'main_app/home.html')

def about_view(request):
    """View for the About page"""
    return render(request, 'main_app/about.html')

def contact_view(request):
    """View for the Contact page"""

    return render(request, 'main_app/contact.html')
