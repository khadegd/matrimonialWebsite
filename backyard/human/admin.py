from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from human.forms import UserCreationForm, UserChangeForm

UserModel = get_user_model()

class UserAdmin(BaseUserAdmin):
    model = UserModel
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'first_name', 'last_name', 'contact', 'email', 'is_staff')

    # fieldsets = BaseUserAdmin.fieldsets
    fieldsets = (
            (None, {'fields': ('username', 'password')}),
            (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'contact')}),
            (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
            (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'contact', 'password1', 'password2')}
        ),
    )

    def get_fieldsets(self, request, obj=None):
        if not request.user.is_superuser:
            return self.get_staff_fieldsets()
        else:
            return super(UserAdmin, self).get_fieldsets(request, obj)

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return self.get_staff_readonly_fields()
        else:
            return super(UserAdmin, self).get_readonly_fields(request, obj)

    def get_staff_fieldsets(self):
        staff_fieldsets = (
                (None, {'fields': ('username', 'password')}),
                (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'contact')}),
                (_('Permissions'), {'fields': ('is_active',)}),
                (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        )
        return staff_fieldsets

    def get_staff_readonly_fields(self):
        staff_readonly_fields = ('username', 'email', 'contact', 'last_login', 'date_joined')
        return staff_readonly_fields

    def get_queryset(self, request):
        if request.user.is_superuser:
            return UserModel.objects.all()
        elif request.user.is_staff:
            return UserModel.objects.filter(is_staff=False)

admin.site.register(UserModel, UserAdmin)
