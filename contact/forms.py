from django import forms

from .models import User


class UserForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    content = forms.CharField(required=False)
    title = forms.CharField(required=False)
    location = forms.CharField(required=False)


class JoinForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
