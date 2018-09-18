from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.contrib.auth import get_user_model

UserModel = get_user_model()
class UserCreationForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'contact') + BaseUserCreationForm.Meta.fields 

class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = UserModel
        fields = ('email', 'contact') + BaseUserCreationForm.Meta.fields

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
