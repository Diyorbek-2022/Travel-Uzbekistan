import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    # Custom email validation
    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Basic email regex pattern to check format
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        # Check if email format is valid
        if not re.match(email_regex, email):
            raise ValidationError(
                "Неверный формат электронной почты. Пожалуйста, введите действительный адрес электронной почты.")
        return email
