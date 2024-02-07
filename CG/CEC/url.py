
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('login',views.login, name="login"),
    path('signup',views.signup, name="signup"),
    path('postsign/',views.postsign,name ="postsign"),
    path('presign/',views.presign,name ="presign"),
    path('calculator',views.calculator, name="calculator"),
]
