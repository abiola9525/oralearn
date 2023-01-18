from django.urls import path
from . import views
from .views import GdListView, GdDetailView, GdCreateView, GdUpdateView, GdDeleteView

urlpatterns = [
    # path('', views.home, name="gd-home"),
    path('about', views.about, name="gd-about"),
    path('contact', views.contact, name="gd-contact"),


    path('gd', GdListView.as_view(), name="gd-home"),
    path('gd-new', GdCreateView.as_view(), name="gd-new"),
    path('gd/<int:pk>', GdDetailView.as_view(), name="gd-detail"),
    path('gd/<int:pk>/update', GdUpdateView.as_view(), name="gd-update"),
    path('gd/<int:pk>/delete', GdDeleteView.as_view(), name="gd-delete")
]
