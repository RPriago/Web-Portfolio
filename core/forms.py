from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'custom-form-input',
            'placeholder': 'John Max',
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'custom-form-input',
            'placeholder': 'example@example.com',
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'custom-form-textarea',
            'placeholder': 'Message',
        })
   )