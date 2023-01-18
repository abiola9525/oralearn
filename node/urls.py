from django.urls import path
from . import views
from .views import NodeListView, NodeDetailView, NodeCreateView, NodeUpdateView, NodeDeleteView

urlpatterns = [
    # path('', views.home, name="node-home"),
    path('about', views.about, name="node-about"),
    path('contact', views.contact, name="node-contact"),


    path('node', NodeListView.as_view(), name="node-home"),
    path('node-new', NodeCreateView.as_view(), name="node-new"),
    path('node/<int:pk>', NodeDetailView.as_view(), name="node-detail"),
    path('node/<int:pk>/update', NodeUpdateView.as_view(), name="node-update"),
    path('node/<int:pk>/delete', NodeDeleteView.as_view(), name="node-delete")
]
