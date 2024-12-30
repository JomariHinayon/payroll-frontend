from django.shortcuts import render
from .models import Announcement

def announcement_view(request):
    announcement = Announcement.objects.last()  # Get the latest announcement
    return render(request, 'announcement.html', {'announcement': announcement})
