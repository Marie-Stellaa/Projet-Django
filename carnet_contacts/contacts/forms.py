from django import forms
from .models import Contact
import re

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'prenom', 'email', 'telephone']

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        if telephone and not re.match(r'^\d{10}$', telephone):
            raise forms.ValidationError("Le numéro doit contenir exactement 10 chiffres.")
        return telephone