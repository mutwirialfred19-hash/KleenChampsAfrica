from django import forms
from .models import ContactInquiry

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInquiry
        fields = ['full_name', 'email', 'phone', 'company', 'service', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+254 7XX XXX XXX'}),
            'company': forms.TextInput(attrs={'placeholder': 'Company or property name (optional)'}),
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Tell us about your project — location, surface type, current condition...'}),
        }
