from django.shortcuts import render


def event_map(request):
    return render(request, 'maps/event_map.html')


def jaksafe_map(request):
    return render(request, 'maps/jaksafe_map.html')
