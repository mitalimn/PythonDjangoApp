from django.shortcuts import render

# Create your views here.


 # SnippetApp/views.py
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)