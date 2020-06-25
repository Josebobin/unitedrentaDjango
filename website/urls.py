from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('equipments/', views.equipments, name="equipments"),
    path('constructions/', views.construction, name="constructions"),
    path('transport/', views.transportproduct, name="transport"),
    path('lifting/', views.liftingproduct, name="lifting"),
    path('onroad/', views.onroadproducts, name="onroad"),
    path('enquiry/', views.enquiry, name="enquiry"),
    path('contact/', views.contact, name="contact"),
    path('test/', views.test, name="test"),




]
