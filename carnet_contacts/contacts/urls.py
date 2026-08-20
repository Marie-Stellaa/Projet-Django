from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_contacts, name='liste_contacts'),
    path('ajouter/', views.creer_contact, name='creer_contact'),
    path('modifier/<int:contact_id>/', views.modifier_contact, name='modifier_contact'),
    path('supprimer/<int:contact_id>/', views.supprimer_contact, name='supprimer_contact'),
    path('<int:contact_id>/', views.detail_contact, name='detail_contact'),

]
