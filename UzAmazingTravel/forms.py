from django import forms

from UzAmazingTravel.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        # fields = '__all__'
