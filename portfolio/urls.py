from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('showcase/', views.showcase, name='portfolio-showcase'),
]