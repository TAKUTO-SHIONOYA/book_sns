from django.contrib.auth import forms as auth_forms
from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password', 'password2')
