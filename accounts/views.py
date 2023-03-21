# from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from allauth.account.views import PasswordChangeView
from django.contrib import messages

# D5 user
# from django.contrib.auth.models import User
from .models import CustomUser
from .forms import CustomUserUpdateForm, CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Sign Up view
# class SignUpView(generic.CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'

class CustomUserView(LoginRequiredMixin, generic.DetailView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'account/profile.html'


class CustomUserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    template_name = 'account/profile_edit.html'
    form_class = CustomUserUpdateForm

    def get_object(self, queryset=None):
        return self.request.user


class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('profile')
