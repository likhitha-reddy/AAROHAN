from django.shortcuts import render
from .models import Events, EventCategory, Workshops
# Create your views here.

def index(request):
    events = Events.objects.all()
    workshops = Workshops.objects.all()
    context = {'events': events, 'workshops': workshops}
    return render(request, 'flow/home.html', context)

def eventGroups(request):
    eventGroups = EventCategory.objects.all()
    context = {'event_groups':eventGroups}
    return render(request,'flow/categories.html',context)

def events(request, gId):
    events = Events.objects.filter(eventGroup=EventCategory.objects.get(groupId=gID))
    context = {'events':events}
    return render(request,'flow/category.html',context)







