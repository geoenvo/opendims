from django.shortcuts import render
from django.views import generic
from django.conf import settings

from rest_framework import generics, filters

from .models import Contact

class ContactListView(generic.ListView):
    queryset = ContactForm.objects.order_by('-created')
    paginate_by = settings.ITEMS_PER_PAGE


class ContactDetailView(generic.DetailView):
    model = ContactForm
