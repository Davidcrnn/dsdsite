from django import forms


class MessageForm(forms.Form):
    nom = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True, label='Votre email')
    phone = forms.CharField(max_length=10)
    objet = forms.CharField(required=True, label='Objet du message')
    message = forms.CharField(widget=forms.Textarea,
                              required=True, label='Votre message')


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
