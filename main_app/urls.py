from django.urls import path
ftom . import views

urlpatterns = [
  path('', views.Home.as_view(), name="home") 
]