from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# D5 user
from django.contrib.auth.models import User
from .forms import CustomUserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Sign Up view
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CustomUserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = 'account/profile.html'
    form_class = CustomUserUpdateForm
