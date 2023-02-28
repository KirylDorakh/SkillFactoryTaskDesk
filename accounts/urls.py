from django.urls import path
from .views import SignUpView, CustomUserUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/edit', CustomUserUpdateView.as_view(), name='profile')
]