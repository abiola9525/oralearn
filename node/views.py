from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Node
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# def home(request):
#     context = {
#         'Nodes': Node.objects.all()
#     }
#     return render(request, 'node/home.html', context)


def about(request):
    return render(request, 'node/about.html', {'title': "About Page"})
def contact(request):
    return render(request, 'node/contact.html', {'title': "Contact Page"})

class NodeListView(LoginRequiredMixin, ListView):
    model = Node
    template_name = 'node/home.html'
    context_object_name = 'nodes'
    ordering = ["-date_posted"]


class NodeDetailView(LoginRequiredMixin, DetailView):
    model = Node


class NodeCreateView(LoginRequiredMixin, CreateView):
    model = Node
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     Node = self.get_object()
    #     if self.request.user == Node.author:
    #         return True
    #     return False


class NodeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Node
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        node = self.get_object()
        if self.request.user == node.author:
            return True
        return False


class NodeDeleteView(DeleteView):
    model = Node
    success_url = '/'

    def test_func(self):
        node = self.get_object()
        if self.request.user == node.author:
            return True
        return False
