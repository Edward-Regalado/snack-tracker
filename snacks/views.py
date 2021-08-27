from django.db import models
from django.views.generic import ListView, DetailView
from .models import Snacks

# Create your views here.

class SnackListViews(ListView):
    template_name = 'snack_list.html'
    model = Snacks
    # context_object_name = 'sw_snacks'
    
class SnackDetailViews(DetailView):
    template_name = 'snack_detail.html'
    model = Snacks