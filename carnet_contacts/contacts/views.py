from django.shortcuts import render, get_object_or_404
from .models import Contact

def liste_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/liste_contacts.html', {'contacts': contacts})

def detail_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contacts/detail_contacts.html', {'contact': contact})