from django.shortcuts import render
from django.views import generic
# Create your views here.

from django.contrib.auth import get_user_model


USER_MODEL = get_user_model()

class ProfileView(generic.DetailView):
    model = USER_MODEL
    template_name = 'users/profile.html'
    context_object_name = 'user'
