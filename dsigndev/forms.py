from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'contact-input'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Objet',
        'class': 'contact-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 5,
        'placeholder': 'Votre message',
        'class': 'contact-input '}))
