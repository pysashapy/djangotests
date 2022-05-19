from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    path('description/<str:type>/<str:version>', views.getDescription),

]
