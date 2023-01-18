from django.urls import path
from . import views
from .views import JSListView, JSDetailView, JSCreateView, JSUpdateView, JSDeleteView

urlpatterns = [
    # path('', views.home, name="js-home"),
    path('about', views.about, name="js-about"),
    path('contact', views.contact, name="js-contact"),


    path('js', JSListView.as_view(), name="js-home"),
    path('js-new', JSCreateView.as_view(), name="js-new"),
    path('js/<int:pk>', JSDetailView.as_view(), name="js-detail"),
    path('js/<int:pk>/update', JSUpdateView.as_view(), name="js-update"),
    path('js/<int:pk>/delete', JSDeleteView.as_view(), name="js-delete")
]
