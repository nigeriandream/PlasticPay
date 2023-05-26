from django.urls import path

from .views import *


urlpatterns = [
    path("", home_view, name="home"),
    path("recycler_portal", recycler_portal, name="recycler_portal"),
    path("support_recycler", support_recycler, name="support_recycler"),
    path("recycle_data", recycle_data, name="recycle_data"),
]
