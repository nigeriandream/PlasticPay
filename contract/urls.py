from django.urls import path

from .views import *


urlpatterns = [
    path("connectWallet/", connect_wallet, name="connectWallet"),
]
