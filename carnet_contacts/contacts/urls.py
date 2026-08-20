from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.liste_contacts, name='liste_contacts'),
    path('ajouter/', views.creer_contact, name='creer_contact'),
    path('modifier/<int:contact_id>/', views.modifier_contact, name='modifier_contact'),
    path('supprimer/<int:contact_id>/', views.supprimer_contact, name='supprimer_contact'),
    path('<int:contact_id>/', views.detail_contact, name='detail_contact'),
    path('admin/', admin.site.urls),
    path('contacts/', include('contacts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
