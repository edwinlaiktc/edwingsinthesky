from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Track


def home(request):
    track_list = Track.objects.order_by('name')
    context = {
        'track_list': track_list,
    }
    return render(request, 'music_center/home.html', context)


def album(request, album_name):
    response = f'This album is {album_name}'
    return HttpResponse(response)
