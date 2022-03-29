from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from .models import Dsc

from django.views.generic import  DeleteView, ListView, DetailView, CreateView, UpdateView


def index(requezst):
    return HttpResponse("<h1>Welecome to Dsc</h1>")

class IndexView(View):
    def get(self, request):
         return HttpResponse("<h1>Welecome to Dsc (Class Based)</h1>")

class StudentListView(ListView):
    model = Dsc
    paginate_by = 2
    template_name = 'listview.html'


class StudentDetailView(DetailView):
    model = Dsc
    context_object_name = "Student"
    template_name = 'detailview.html'

class StudentCreateView(CreateView):
    model = Dsc
    fields = ['name', 'age']
    template_name = 'createview.html'

class StudentUpdateView(UpdateView):
    model = Dsc
    fields = ['name', 'age']
    template_name = 'createview.html'

class StudentDeleteView(DeleteView):
    model = Dsc
    fields = ['name', 'author']
    template_name = 'confirm.html'
    success_url = '/'



