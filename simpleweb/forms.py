from django import forms
from django.core.exceptions import ValidationError

from .validators import validate_domain_name, phone_regex

class ContactForm(forms.Form):
    name = forms.CharField(max_length=130, label="Name")
    email = forms.EmailField(label="Email Address", validators=[validate_domain_name])
    company = forms.CharField(max_length=40, label="School/Company")
    phone = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'+254..'}), max_length=13, label="Phone", validators=[phone_regex])
    message = forms.CharField(widget = forms.Textarea, label="Message")

