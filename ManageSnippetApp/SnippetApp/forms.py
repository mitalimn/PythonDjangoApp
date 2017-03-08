from django import forms
from .models import Snippet
class CreateSnippet(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'language', 'code_snippet', 'description']

