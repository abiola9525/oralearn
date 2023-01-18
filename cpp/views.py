from django.shortcuts import render
from django.http import HttpResponse
from .models import Cpp
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# def home(request):
#     context = {
#         'posts': Cpp.objects.all()
#     }
#     return render(request, 'cpp/home.html', context)


def about(request):
    return render(request, 'cpp/about.html', {'title': "About Page"})
def contact(request):
    return render(request, 'cpp/contact.html', {'title': "Contact Page"})

class CppListView(LoginRequiredMixin, ListView):
    model = Cpp
    template_name = 'cpp/home.html'
    context_object_name = 'cpps'
    ordering = ["-date_posted"]


class CppDetailView(LoginRequiredMixin, DetailView):
    model = Cpp


class CppCreateView(LoginRequiredMixin, CreateView):
    model = Cpp
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     Cpp = self.get_object()
    #     if self.request.user == Cpp.author:
    #         return True
    #     return False


class CppUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cpp
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        cpp = self.get_object()
        if self.request.user == cpp.author:
            return True
        return False


class CppDeleteView(DeleteView):
    model = Cpp
    success_url = '/'

    def test_func(self):
        cpp = self.get_object()
        if self.request.user == cpp.author:
            return True
        return False
