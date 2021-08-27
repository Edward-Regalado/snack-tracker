from django.urls import path
# from django.urls.resolvers import URLPattern
from .views import SnackListViews, SnackDetailViews

urlpatterns = [
    path('', SnackListViews.as_view(), name = 'snack_list'),
    path('<int:pk>/', SnackDetailViews.as_view(), name = 'snack_detail'),
]