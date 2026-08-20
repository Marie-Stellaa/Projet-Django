from django.shortcuts import render, get_object_or_404
from .models import Contact
from .forms import ContactForm 

def liste_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/liste_contacts.html', {'contacts': contacts})

def detail_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contacts/detail_contacts.html', {'contact': contact})
def creer_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts/form_contact.html', {'form': form, 'titre': 'Ajouter un contact'})

def modifier_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('detail_contact', contact_id=contact.id)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/form_contact.html', {'form': form, 'titre': 'Modifier le contact'})

def supprimer_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        contact.delete()
        return redirect('liste_contacts')
    return render(request, 'contacts/confirmer_suppression.html', {'contact': contact})