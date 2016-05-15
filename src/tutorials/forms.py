from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput({"placeholder": "Name"}))
    email = forms.EmailField(widget=forms.TextInput({"placeholder": "Email"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}))


