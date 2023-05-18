from django.urls import path
from .views import HomePageView, AboutPageView, EmailPageView, PhonePageView

urlpatterns = [
    path('phone/', PhonePageView.as_view(), name='phone'),
    path('email/', EmailPageView.as_view(), name='email'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]