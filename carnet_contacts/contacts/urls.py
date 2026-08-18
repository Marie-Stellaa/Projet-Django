from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_contacts, name='liste_contacts'),
    path('<int:contact_id>/', views.detail_contact, name='detail_contact'),
]
