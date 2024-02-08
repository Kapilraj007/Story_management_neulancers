from django.forms import ModelForm
from .models import Story_Management

class StoryForm(ModelForm):
    class Meta:
        model = Story_Management
        fields = '__all__'
        exclude = ['user']