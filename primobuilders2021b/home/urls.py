from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('about/', views.about, name='About'),
    path('services/', views.services, name='Services'),
    path('areasOfServ/', views.areasOfServ, name='areasOfServ'),
    path('consultation', views.consultation, name='consultation'),

]
