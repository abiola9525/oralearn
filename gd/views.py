from django.shortcuts import render
from django.http import HttpResponse
from .models import Gd
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# def home(request):
#     context = {
#         'posts': Gd.objects.all()
#     }
#     return render(request, 'gd/home.html', context)


def about(request):
    return render(request, 'gd/about.html', {'title': "About Page"})
def contact(request):
    return render(request, 'gd/contact.html', {'title': "Contact Page"})

class GdListView(LoginRequiredMixin, ListView):
    model = Gd
    template_name = 'gd/home.html'
    context_object_name = 'gds'
    ordering = ["-date_posted"]


class GdDetailView(LoginRequiredMixin, DetailView):
    model = Gd


class GdCreateView(LoginRequiredMixin, CreateView):
    model = Gd
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     Gd = self.get_object()
    #     if self.request.user == Gd.author:
    #         return True
    #     return False


class GdUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Gd
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        gd = self.get_object()
        if self.request.user == gd.author:
            return True
        return False


class GdDeleteView(DeleteView):
    model = Gd
    success_url = '/'

    def test_func(self):
        gd = self.get_object()
        if self.request.user == gd.author:
            return True
        return False
