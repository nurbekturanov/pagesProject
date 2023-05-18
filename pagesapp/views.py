from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class EmailPageView(TemplateView):
    template_name = 'email.html'

class PhonePageView(TemplateView):
    template_name = 'phone.html'