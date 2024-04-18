from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import teacher

class teacherForm(ModelForm):
    class Meta:
        model = teacher
        fields='__all__'
        exclude=['user','slug','active']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = {'username','email','password1','password2'}