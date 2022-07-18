from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_doc, name="input_doc"),
    path('thankyou',views.input_doc,name="input_doc"),
]