from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import teacher

class teacherForm(ModelForm):
    class Meta:
        model = teacher
        fields=('name','studio','message','about','phone_number','photo','email')