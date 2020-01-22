from django import forms


class MessageForm(forms.Form):
    nom = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True, label='Votre email')
    phone = forms.CharField(max_length=10)
    objet = forms.CharField(required=True, label='Objet du message')
    message = forms.CharField(widget=forms.Textarea,
                              required=True, label='Votre message')


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True, label='Votre email')
    subject = forms.CharField(required=True, label='Objet du message')
    message = forms.CharField(widget=forms.Textarea,
                              required=True, label='Votre message')
