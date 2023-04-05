# D5 user
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


# D5 user
class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')


class CustomUserAdminForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
        )


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'email',
            'username',
        )
