# D5 user
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


# D5 user
class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
        )
