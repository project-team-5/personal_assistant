from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import AllContact, Phone, Email
from .forms import AllContactForm, PhoneFormSet, EmailFormSet
from datetime import date, timedelta

def home(request):
    return render(request, 'addressbook/home.html')

def add_contact(request):
    if request.method == 'POST':
        all_contact_form = AllContactForm(request.POST)
        phone_formset = PhoneFormSet(request.POST)
        email_formset = EmailFormSet(request.POST)
        if all_contact_form.is_valid() and phone_formset.is_valid() and email_formset.is_valid():
            all_contact = all_contact_form.save(commit=False)
            all_contact.host_id = 4
            all_contact.save()
            phone_formset.instance = all_contact
            phone_formset.save()
            email_formset.instance = all_contact
            email_formset.save()
            messages.success(request, 'Contact saved successfully!')
            return redirect('home')
    else:
        all_contact_form = AllContactForm()
        phone_formset = PhoneFormSet()
        email_formset = EmailFormSet()
    return render(request, 'addressbook/add_contact.html', {
        'all_contact_form': all_contact_form,
        'phone_formset': phone_formset,
        'email_formset': email_formset
    })

def birthday_list(request):
    if request.method == 'POST':
        days = int(request.POST['days'])
        target_date = date.today() + timedelta(days=days)
        contacts = AllContact.objects.filter(birthday__day=target_date.day, birthday__month=target_date.month)
        return render(request, 'addressbook/birthday_list.html', {'contacts': contacts, 'days': days})
    return render(request, 'addressbook/birthday_form.html')

def search_contact(request):
    query = request.GET.get('q')
    if query:
        contacts = AllContact.objects.filter(fullname__icontains=query)
    else:
        contacts = []
    return render(request, 'addressbook/search_contact.html', {'contacts': contacts})


def contact_list(request):
    contacts = AllContact.objects.all()
    return render(request, 'addressbook/contact_list.html', {'contacts': contacts})

def edit_contact(request, pk):
    contact = get_object_or_404(AllContact, pk=pk)
    if request.method == 'POST':
        all_contact_form = AllContactForm(request.POST, instance=contact)
        phone_formset = PhoneFormSet(request.POST, instance=contact)
        email_formset = EmailFormSet(request.POST, instance=contact)
        if all_contact_form.is_valid() and phone_formset.is_valid() and email_formset.is_valid():
            all_contact = all_contact_form.save(commit=False)
            all_contact.host_id = contact.host_id
            all_contact.save()
            phone_formset.instance = all_contact
            phone_formset.save()
            email_formset.instance = all_contact
            email_formset.save()
            messages.success(request, 'Contact updated successfully!')
            return redirect('contact_list')
    else:
        all_contact_form = AllContactForm(instance=contact)
        phone_formset = PhoneFormSet(instance=contact)
        email_formset = EmailFormSet(instance=contact)
    return render(request, 'addressbook/edit_contact.html', {
        'all_contact_form': all_contact_form, 
        'phone_formset': phone_formset,
        'email_formset': email_formset,
        'contact': contact
    })

def delete_contact(request, pk):
    contact = get_object_or_404(AllContact, pk=pk)
    contact.delete()
    messages.success(request, 'Contact deleted successfully!')
    return redirect('contact_list')

