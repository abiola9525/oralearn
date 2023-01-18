from django.urls import path
from . import views
from .views import PydjangoListView, PydjangoDetailView, PydjangoCreateView, PydjangoUpdateView, PydjangoDeleteView

urlpatterns = [
    # path('', views.home, name="pydjango-home"),
    path('about', views.about, name="pydjango-about"),
    path('contact', views.contact, name="pydjango-contact"),


    path('pydjango', PydjangoListView.as_view(), name="pydjango-home"),
    path('pydjango-new', PydjangoCreateView.as_view(), name="pydjango-new"),
    path('pydjango/<int:pk>', PydjangoDetailView.as_view(), name="pydjango-detail"),
    path('pydjango/<int:pk>/update', PydjangoUpdateView.as_view(), name="pydjango-update"),
    path('pydjango/<int:pk>/delete', PydjangoDeleteView.as_view(), name="pydjango-delete")
]
