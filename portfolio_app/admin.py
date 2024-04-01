from django.contrib import admin
from .models import Student,Portfolio,Project

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Student)
admin.site.register(Project)