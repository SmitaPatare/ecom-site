from django.urls import path
from . import views
from store.views import IndexView
from store.views import Cart
from store.views import logout
from store.views import CheckOut
from store.views import OrderView
from .middleware.auth import auth_middleware



urlpatterns = [
    path("",IndexView.as_view(), name="homepage"),
    path('signup/',views.SignupView.as_view(), name="signup"), #url for class based view
    path('login/',views.loginView.as_view(), name="login"),
    path('cart/',Cart.as_view(), name="cart"),
    path('check-out/',views.CheckOut.as_view(), name="checkout"),
    #path('orders/',OrderView.as_view(), name="orders"),
    path('logout/',logout,name="logout"),

    path('orders/',auth_middleware(OrderView.as_view()), name="orders"),

    

]