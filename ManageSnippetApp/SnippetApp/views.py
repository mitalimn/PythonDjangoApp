from django.shortcuts import render
from django.http import HttpResponseRedirect
 # SnippetApp/views.py
from django.views.generic import TemplateView
from django.shortcuts import Http404

from .models import Snippet
from .forms import CreateSnippet
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        form = CreateSnippet()
        #try:
        snippets = Snippet.objects.all()
        #except snippet.DoesNotExist:
        #raise Http404("Snippets does not exist")
        return render(request, 'index.html', {'form': form, "snippet": snippets})
    def post(self, request, **kwargs):
        form = CreateSnippet(request.POST)
        # verify that form is valid
        if form.is_valid():
        # save the form data to database
            form.save(commit=True)
            snippets = Snippet.objects.all() 
                #snippet.DoesNotExist:
                #raise Http404("Snippets does not exist")
            form = CreateSnippet()
            #print("Snipettttttttttt Language/.............",snippet.title)
        return render(request, 'index.html', {'form': form, "snippet": snippets})
        #################################################################################
          