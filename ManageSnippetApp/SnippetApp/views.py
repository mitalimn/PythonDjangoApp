from django.shortcuts import render
 # SnippetApp/views.py
from django.views.generic import TemplateView

from .models import Snippet
from .forms import CreateSnippet
# Create your views here.


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        form = CreateSnippet()
        return render(request, 'index.html', {'form': form},{'Snippet':Snippet})

def post_new(request):
    if request.method == "POST":
        form = CreateSnippet(request.POST)
        if form.is_valid():
            Snippet = form.save(commit=False)
            Snippet.title = request.title
            Snippet.language = request.language
            Snippet.code_snippet = request.code_snippet
            Snippet.description = request.description
            Snippet.save()
            #return redirect('post_detail', pk=post.pk)
    else:
        form = CreateSnippet()
    return render(request, 'index.html', {'form': form}, {'Snippet':Snippet})        