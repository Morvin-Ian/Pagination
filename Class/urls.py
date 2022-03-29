from django.urls import path
from . import views

from .views import IndexView, StudentListView, StudentDetailView, StudentCreateView, StudentUpdateView, StudentDeleteView
urlpatterns = [
    # path('', views.index, name = 'index'),
    # path('class/', IndexView.as_view(), name = 'indexview'),

    path('', StudentListView.as_view(), name = 'listview'),
    path('<int:pk>', StudentDetailView.as_view(), name = 'detailview'),
    path('create/', StudentCreateView.as_view(), name = 'createview'),
    path('update/<int:pk>', StudentUpdateView.as_view(), name = 'updateview'),
    path('delete/<int:pk>', StudentDeleteView.as_view(), name = 'deleteview'),

]