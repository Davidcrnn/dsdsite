from django.shortcuts import render, redirect

from django.views.generic import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import MessageForm, ContactForm
from django.contrib import messages
from .models import (
    Projet,

)


class HomePageView(View):
    template_name = 'home.html'
    model = Projet

    def get(self, request):
        projets = Projet.objects.order_by('-created_at')
        form = ContactForm()
        context = {
            "projets": projets,
            "form": form,
        }
        return render(request, 'home.html', context)

    def post(self, request):
        if self.request.method == 'GET':
            form = ContactForm()
        else:
            form = ContactForm(self.request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']

                try:
                    send_mail(subject, message, from_email,
                              ['david.crenin@gmail.com'], fail_silently=False)
                    messages.success(
                        request, 'Votre message a été envoyé !')
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('home')
        return render(request, "contact.html", {'form': form},)
