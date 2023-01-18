from django.urls import path
from . import views
from .views import JavaListView, JavaDetailView, JavaCreateView, JavaUpdateView, JavaDeleteView

urlpatterns = [
    path('about', views.about, name="java-about"),
    path('contact', views.contact, name="java-contact"),

    path('java', JavaListView.as_view(), name="java-home"),
    path('java-new', JavaCreateView.as_view(), name="java-new"),
    path('java/<int:pk>', JavaDetailView.as_view(), name="java-detail"),
    path('java/<int:pk>/update', JavaUpdateView.as_view(), name="java-update"),
    path('java/<int:pk>/delete', JavaDeleteView.as_view(), name="java-delete")
]