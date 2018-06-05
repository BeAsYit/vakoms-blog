"""
Module with forms for users
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(forms.Form):
    """
    Here we add new parameter phone to our user on registration stage
    """
    phone = forms.CharField(max_length=15)

    def signup(self, request, user):
        user.phone = self.cleaned_data['phone']
        user.save()

class CustomUserChangeForm(UserChangeForm):
    """
    Change user change form to our form with custom fields
    """
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields