from django.urls import path
from . import views

urlpatterns = [
    path('', views.input ,name="input"),
    path('thankyou',views.input,name="input"),
]