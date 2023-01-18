from django.shortcuts import render
from django.http import HttpResponse
from .models import JS
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# def home(request):
#     context = {
#         'posts': JS.objects.all()
#     }
#     return render(request, 'js/home.html', context)


def about(request):
    return render(request, 'js/about.html', {'title': "About Page"})
def contact(request):
    return render(request, 'js/contact.html', {'title': "Contact Page"})

class JSListView(LoginRequiredMixin, ListView):
    model = JS
    template_name = 'js/home.html'
    context_object_name = 'jss'
    ordering = ["-date_posted"]


class JSDetailView(LoginRequiredMixin, DetailView):
    model = JS


class JSCreateView(LoginRequiredMixin, CreateView):
    model = JS
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     JS = self.get_object()
    #     if self.request.user == JS.author:
    #         return True
    #     return False


class JSUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = JS
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        js = self.get_object()
        if self.request.user == js.author:
            return True
        return False


class JSDeleteView(DeleteView):
    model = JS
    success_url = '/'

    def test_func(self):
        js = self.get_object()
        if self.request.user == js.author:
            return True
        return False
