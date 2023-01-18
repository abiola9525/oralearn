from django.urls import path
from . import views
from .views import CppListView, CppDetailView, CppCreateView, CppUpdateView, CppDeleteView

urlpatterns = [
    # path('', views.home, name="cpp-home"),
    path('about', views.about, name="cpp-about"),
    path('contact', views.contact, name="cpp-contact"),


    path('cpp', CppListView.as_view(), name="cpp-home"),
    path('cpp-new', CppCreateView.as_view(), name="cpp-new"),
    path('cpp/<int:pk>', CppDetailView.as_view(), name="cpp-detail"),
    path('cpp/<int:pk>/update', CppUpdateView.as_view(), name="cpp-update"),
    path('cpp/<int:pk>/delete', CppDeleteView.as_view(), name="cpp-delete")
]
