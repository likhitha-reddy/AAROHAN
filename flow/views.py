from django.shortcuts import render, Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import *
# Create your views here.

def index(request):
    events = Events.objects.all()
    workshops = Workshops.objects.all()
    faqs = FAQ.objects.all()
    about = About.objects.all()
    sponsors = Sponsors.objects.all()
    attractions = MajorAttractions.objects.all()
    context = {'events': events, 'workshops': workshops, 'faqs': faqs, 'about':about, 'sponsors':sponsors, 'attractions': attractions}
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

def sponsor_view(request):
    sponsors = Sponsors.objects.all()
    context = {'sponsors':sponsors}
    return render(request,'flow/sponsors', context)

def about_page(request):
    about = About.objects.all()
    context = {'about':about}
    return render(request,'flow/about.html',context)

def faq_page(request):
    faqs = FAQ.objects.all()
    context = {'faqs':faqs}
    return render(request,"flow/faq.html",context)

def attractions_page(request):
    attractions = MajorAttractions.objects.all()
    context = {'attractions':attractions}
    return render(request,'flow/attractions.html',context)

def team_page(request):
    umbrellas = TeamCategory.objects.all()
    res = []
    for umbrella in umbrellas:
        members = TeamMember.objects.filter(team=umbrella)
        group = {'name':umbrella.name , 'members':members}
        res.append(group)
    context = {'teams':res}
    return render(request,"flow/teams.html", context)
