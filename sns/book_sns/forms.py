from django.contrib.auth import forms as auth_forms
from django import forms

class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label
class UserCreateForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput())
