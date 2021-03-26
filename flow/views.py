from django.shortcuts import render, Http404
from django.core.exceptions import ObjectDoesNotExist
from .models import *
# Create your views here.

def index(request):
    workshops = Workshops.objects.all()
    faqs = FAQ.objects.all()
    about = About.objects.all()
    sponsors = Sponsors.objects.all()
    attractions = MajorAttractions.objects.all()
    context = {'workshops': workshops, 'faqs': faqs, 'about':about, 'sponsors':sponsors, 'attractions': attractions}
    return render(request, 'flow/index.html', context)

def home(request):
    events = EventCategory.objects.all()
    workshops = Workshops.objects.all()
    faqs = FAQ.objects.all()
    about = About.objects.all()
    sponsors = Sponsors.objects.all()
    attractions = MajorAttractions.objects.all()
    context = {'events': events, 'workshops': workshops, 'faqs': faqs, 'about':about, 'sponsors':sponsors, 'attractions': attractions}
    return render(request, 'flow/home.html', context)
    
def events(request, id):
    context = {}
    try:
        categrory = EventCategory.objects.get(groupId=id)
        events = Events.objects.filter(eventGroup=categrory)
        context['events'] = events
        context['group'] = categrory
        return render(request,'flow/events.html',context)
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
    return render(request,'flow/aboutus.html',context)
def contactus(request):
    return render(request,'flow/contactus.html')
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
    members = []
    for umbrella in umbrellas:
        members.append((TeamMember.objects.filter(team=umbrella).values()))
    umbrellas=TeamCategory.objects.values()
    umbrellas=[umbrella for umbrella in umbrellas]
    members_list=[]
    for category in members:
        category_members=[member for member in category]
        members_list.append(category_members)
    context = {'teams':umbrellas,'members':members_list}
    return render(request,"flow/teampage.html", context)

def timeline(request):
    days = Timeline.objects.all()
    return render(request, 'flow/timeline2.html', {'days': days})

def timeline_detail(request, id):
    day = Timeline.objects.get(day_number=id)
    events = Events.objects.filter(eventDay__day_number__exact=id).order_by('date_time')
    context = {'day': day, 'events': events}
    return render(request, 'flow/event_timeline2.html', context)