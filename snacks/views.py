from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snacks

# Create your views here.

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snacks
    context_object_name = 'sw_snacks'
    
class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snacks