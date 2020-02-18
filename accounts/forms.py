from django.forms import ModelForm
from django.contrib.auth import get_user_model

user = get_user_model()


class SignUpForm(ModelForm):
    class Meta:
        model = user
        fields = ['first_name','last_name','email', 'image', 'phone', 'password']

