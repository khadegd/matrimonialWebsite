from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend:
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            import pdb; pdb.set_trace()
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
