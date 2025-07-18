from django.urls import path
from .views import store_home
from . import views
urlpatterns = [
    path('',store_home,name='store_home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('cart/',views.cart_view,name='cart'), 
    path('about/',views.about_view,name='about')

]


