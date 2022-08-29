from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path("accounts/user/signup/", views.user_signup_view, name='user_account_signup'),
    path("accounts/shop/signup/", views.shop_signup_view, name='shop_account_signup'),
    
    path("accounts/", include("allauth.urls")),
]
