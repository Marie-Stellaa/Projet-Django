from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_contacts, name='liste_contacts'),
    path('<int:pk>/', views.detail_contacts, name='detail_contacts'),
    path('ajouter/', views.ajouter_contact, name='ajouter_contact'),
    path('<int:pk>/modifier/', views.modifier_contact, name='modifier_contact'),
    path('<int:pk>/supprimer/', views.supprimer_contact, name='supprimer_contact'),
]