from django.shortcuts import render
from django.http import HttpResponse
from .models import Java
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def about(request):
    return render(request, 'java/about.html', {'title': "About Page"})
def contact(request):
    return render(request, 'java/contact.html', {'title': "Contact Page"})

class JavaListView(LoginRequiredMixin, ListView):
    model = Java
    template_name = 'java/home.html'
    context_object_name =  'javas'
    ordering = ["-date_posted"]
    
class JavaDetailView(LoginRequiredMixin, DetailView):
    model = Java
    
class JavaCreateView(LoginRequiredMixin, CreateView):
    model = Java
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
class JavaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Java
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        java = self.get_object()
        if self.request.user == java.author:
            return True
        return False

class JavaDeleteView(DeleteView):
    model = Java
    success_url = '/'

    def test_func(self):
        java = self.get_object()
        if self.request.user == java.author:
            return True
        return False