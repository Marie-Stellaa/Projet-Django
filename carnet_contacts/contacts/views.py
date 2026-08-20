from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

def liste_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/liste_contacts.html', {'contacts': contacts})

def detail_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/detail_contact.html', {'contact': contact})

@login_required
def ajouter_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)  # request.FILES obligatoire pour l'upload
        if form.is_valid():
            form.save()
            messages.success(request, "Contact ajouté avec succès.")
            return redirect('liste_contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts/form_contact.html', {'form': form, 'titre': 'Ajouter un contact'})

@login_required
def modifier_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact modifié avec succès.")
            return redirect('detail_contact', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/form_contact.html', {'form': form, 'titre': 'Modifier le contact'})

@login_required
def supprimer_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        messages.success(request, "Contact supprimé avec succès.")
        return redirect('liste_contacts')
    return render(request, 'contacts/confirmer_suppression.html', {'contact': contact})