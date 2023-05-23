from django.urls import path
from . import views

urlpatterns = [
    path('connectWallet/', views.connect_wallet, name='connectWallet'),
]