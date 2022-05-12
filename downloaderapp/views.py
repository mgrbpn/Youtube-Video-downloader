from django.shortcuts import render
from django.contrib import messages
from pytube import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        url = request.POST['url']
        YouTube(url).streams.get_highest_resolution().download('../Videos')
        messages.info(request, 'Video Downloaded...')
        return render(request, 'index.html')
    return render(request, 'index.html')
    