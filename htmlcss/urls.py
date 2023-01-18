from django.urls import path
from . import views
from .views import HtmlListView, HtmlDetailView, HtmlCreateView, HtmlUpdateView, HtmlDeleteView

urlpatterns = [
    path('about', views.about, name="html-about"),
    path('contact', views.contact, name="html-contact"),

    path('html', HtmlListView.as_view(), name="html-home"),
    path('html-new', HtmlCreateView.as_view(), name="html-new"),
    path('html/<int:pk>', HtmlDetailView.as_view(), name="html-detail"),
    path('html/<int:pk>/update', HtmlUpdateView.as_view(), name="html-update"),
    path('html/<int:pk>/delete', HtmlDeleteView.as_view(), name="html-delete")
]