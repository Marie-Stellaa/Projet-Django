import re
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nom', 'prenom', 'email', 'telephone', 'adresse', 'photo']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    # Validation personnalisée : format de l'email (en plus de la vérif native d'EmailField)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(regex, email):
            raise forms.ValidationError("Le format de l'email n'est pas valide.")
        return email

    # Validation personnalisée : longueur du numéro de téléphone
    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        # on retire les espaces pour compter uniquement les chiffres
        chiffres = telephone.replace(' ', '').replace('-', '')
        if not chiffres.isdigit():
            raise forms.ValidationError("Le téléphone ne doit contenir que des chiffres.")
        if len(chiffres) != 10:
            raise forms.ValidationError("Le numéro de téléphone doit contenir exactement 10 chiffres.")
        return telephone