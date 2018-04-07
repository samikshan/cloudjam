from django.shortcuts import render
from .models import Sound

def home(request):
    sounds = Sound.objects.all()
    return render(request, 'home.html', {'sounds': sounds})
