from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_exists = User.objects.filter(email=email).exists()
        if user_exists:
            raise forms.ValidationError('Um usuário com este e-mail já existe!')
        return email