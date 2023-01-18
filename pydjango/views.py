from django.shortcuts import render
from django.http import HttpResponse
from .models import Pydjango
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# def home(request):
#     context = {
#         'pydjangos': Pydjango.objects.all()
#     }
#     return render(request, 'pydjango/home.html', context)


def about(request):
    return render(request, 'pydjango/about.html', {'title': "About Page"})
def contact(request):
    return render(request, 'pydjango/contact.html', {'title': "Contact Page"})

class PydjangoListView(LoginRequiredMixin, ListView):
    model = Pydjango
    template_name = 'pydjango/home.html'
    context_object_name = 'pydjangos'
    ordering = ["-date_posted"]


class PydjangoDetailView(LoginRequiredMixin, DetailView):
    model = Pydjango


class PydjangoCreateView(LoginRequiredMixin, CreateView):
    model = Pydjango
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     pydjango = self.get_object()
    #     if self.request.user == pydjango.author:
    #         return True
    #     return False


class PydjangoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pydjango
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        pydjango = self.get_object()
        if self.request.user == pydjango.author:
            return True
        return False


class PydjangoDeleteView(DeleteView):
    model = Pydjango
    success_url = '/'

    def test_func(self):
        pydjango = self.get_object()
        if self.request.user == pydjango.author:
            return True
        return False
