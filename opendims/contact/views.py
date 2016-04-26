from django.shortcuts import render
from django.views import generic
from django.conf import settings

from rest_framework import generics, filters

from .forms import ContactForm


def Contact_new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return render(request, 'contact/contact_complete.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_new.html', {'form': form})
