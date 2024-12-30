from django.urls import path
from .views import announcement_view

urlpatterns = [
    path('', announcement_view, name='announcement'),
]
