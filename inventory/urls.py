from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bike/<int:bike_id>/', views.bike_detail, name='bike_detail'),
]
