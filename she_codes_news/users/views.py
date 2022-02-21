from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

# Create your views here.




USER_MODEL = get_user_model()

class ProfileView(generic.DetailView):
    model = USER_MODEL
    template_name = 'users/profile.html'
    context_object_name = 'user'

class CreateAccountView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "users/createAccount.html"
