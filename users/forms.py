from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(forms.Form):
    phone = forms.CharField(max_length=15)

    def signup(self, request, user):
        user.phone = self.cleaned_data['phone']
        user.save()

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields