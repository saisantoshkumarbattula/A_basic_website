from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Santhu Admin"
admin.site.site_title = "Santhu Admin Portal"
admin.site.index_title = "Welcome to Santhu Portal"

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("rating",views.rating,name="rating"),
    path("chatwithus",views.chat_with_us,name="chatwithus"),
    path("registeracomplaint",views.register_a_complaint,name="registeracomplaint"),

    
    
]