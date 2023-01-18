from django.shortcuts import render
from django.http import HttpResponse
from .models import Html
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def about(request):
    return render(request, 'html/about.html', {'title': "About Page"})
def contact(request):
    return render(request, 'html/contact.html', {'title': "Contact Page"})

class HtmlListView(LoginRequiredMixin, ListView):
    model = Html
    template_name = 'htmlcss/home.html'
    context_object_name =  'htmls'
    ordering = ["-date_posted"]
    
class HtmlDetailView(LoginRequiredMixin, DetailView):
    model = Html
    
class HtmlCreateView(LoginRequiredMixin, CreateView):
    model = Html
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class HtmlUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Html
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        html = self.get_object()
        if self.request.user == html.author:
            return True
        return False

class HtmlDeleteView(DeleteView):
    model = Html
    success_url = '/'

    def test_func(self):
        html = self.get_object()
        if self.request.user == html.author:
            return True
        return False