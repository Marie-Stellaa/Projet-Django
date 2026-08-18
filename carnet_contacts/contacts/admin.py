from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'telephone', 'date_ajout')
    search_fields = ('nom', 'prenom', 'email')
    search_fields = ('nom', 'prenom', 'email')