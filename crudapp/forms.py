from django import forms
from crudapp.models import Task

class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
