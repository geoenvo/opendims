from __future__ import unicode_literals

from django import forms

from captcha.fields import CaptchaField

from .models import Contact


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Contact
        fields = ('name', 'email', 'website', 'subject', 'message',)
