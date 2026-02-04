from django.urls import path
from . import views

urlpatterns = [
    # Static & Information Pages
    path('', views.home_view, name='home'),
    path('collections/', views.collections_view, name='collections'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

    # Authentication Routes
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('place-order/<int:product_id>/', views.place_order, name='place_order'),
]