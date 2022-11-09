from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("tr", tracker1),
    path("la", lada1),
    path("ma/", malibu1),
    path("ca", captiva1),
    path("ji", jip1),
    path("me", mercbenz1),
]
