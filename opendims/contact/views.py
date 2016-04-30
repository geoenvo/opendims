from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _
from django.contrib import messages

from .forms import ContactForm


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                _("Message sent. Thank you for contacting us!")
            )
            return redirect('contact:index')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_index.html', {'form': form})
