import re

from django.db import models
from django.core.exceptions import ValidationError


def validate_telephone(value):
    if not re.match(r'^\d{10}$', value):
        raise ValidationError("Le numéro de téléphone doit contenir exactement 10 chiffres.")


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, blank=True, validators=[validate_telephone])
    photo = models.ImageField(upload_to='contacts_photos/', blank=True, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        ordering = ['nom', 'prenom']