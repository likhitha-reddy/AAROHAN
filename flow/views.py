from django.shortcuts import render, Http404
from django.core.exceptions import ObjectDoesNotExist
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

def events(request, id):
    context = {}
    try:
        categrory = EventCategory.objects.get(groupId=id)
        events = Events.objects.filter(eventGroup=categrory)
        context['events'] = events
        return render(request,'flow/category.html',context)
    except ObjectDoesNotExist:
        raise Http404
    

def workshops(request):
    workshops = Workshops.objects.all()
    context = {'workshops':workshops}
    return render(request,"flow/workshops.html",context)





