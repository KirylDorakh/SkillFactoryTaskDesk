from django.urls import path
from .views import CustomUserUpdateView, CustomUserView, CustomPasswordChangeView

urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>/', CustomUserView.as_view(), name='profile'),
    path('profile/<int:pk>/edit', CustomUserUpdateView.as_view(), name='profile_edit'),
    path('profile/change_password/', CustomPasswordChangeView.as_view(),
         name='profile_change_password'),
]
