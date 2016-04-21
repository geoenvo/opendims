from django.shortcuts import render
from django.views import generic
from django.conf import settings

from rest_framework import generics, filters

from .models import Contact
from .forms import ContactForm


class ContactListView(generic.ListView):
    queryset = Contact.objects.order_by('-created')
    paginate_by = settings.ITEMS_PER_PAGE


class ContactDetailView(generic.DetailView):
    model = Contact

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
