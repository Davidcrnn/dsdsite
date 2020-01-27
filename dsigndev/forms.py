from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'david.crenin@gmail.com',
        'class': 'contact-input'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Projet de création d'un site !",
        'class': 'contact-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 5,
        'placeholder': 'Bonjour, je souhaiterais développer un projet ...',
        'class': 'contact-input '}))
