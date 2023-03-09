from django.shortcuts import render, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
import json

from .models import *


def index(request):
    workshops = Workshops.objects.all()
    faqs = FAQ.objects.all()
    about = About.objects.all()
    sponsors = Sponsors.objects.all()
    attractions = MajorAttractions.objects.all()
    context = {'workshops': workshops, 'faqs': faqs, 'about': about,
               'sponsors': sponsors, 'attractions': attractions}
    return render(request, 'flow/index.html', context)


def home(request):
    workshops = Workshops.objects.all()
    arena = Arena.objects.all()
    faqs = FAQ.objects.all()
    about = About.objects.all()
    sponsors = Sponsors.objects.all()
    attractions = MajorAttractions.objects.all()
    context = {'events': events, 'workshops': workshops, 'faqs': faqs,
               'about': about, 'sponsors': sponsors, 'attractions': attractions, 'arena' : arena}
    return render(request, 'flow/homepage.html', context)


def events(request):
    try:
        days = Timeline.objects.values()
        days = [day for day in days]

        evnt = []
        for d in days:
            evnt.append([eve for eve in Events.objects.filter(eventDay__day_number__exact=d["day_number"]).order_by('date_time').values()])
        
        return render(request, 'flow/eventsAndInitiatives/events.html', {'events':evnt, 'days':list(days)})
    except ObjectDoesNotExist:
        raise Http404


def workshops(request):
    workshops = Workshops.objects.values()
    workshops = [w for w in workshops]
    return render(request, "flow/workshop.html", {'workshops': list(workshops)})

def socialInitiative_view(request):
    socialinitiative = SocialInitiatives.objects.all()
    data=[]
    for i in socialinitiative:
        photos = i.socialImages.all()
        newdictionary = {"socialinitiative":i}
        newdictionary.update({"photos":photos})
        data.append(newdictionary)
    return render(request, "flow/eventsAndInitiatives/socialInitiatives.html", {"data":data})

def industrialvisit_view(request):
    industrialvisits = IndustrialVisits.objects.all()
    data=[]
    for i in industrialvisits:
        photos = i.industrialImages.all()
        newdictionary = {"industrialvisit":i}
        newdictionary.update({"photos":photos})
        data.append(newdictionary)
    return render(request, "flow/eventsAndInitiatives/industrialVisits.html", {"data":data})
    

def sponsor_view(request):
    sponsors = Sponsors.objects.all()
    context = {'sponsors': sponsors}
    return render(request, 'flow/sponsor.html', context)


def about_page(request):
    about = About.objects.all()
    context = {'about': about}
    return render(request, 'flow/aboutus.html', context)


def contactus(request):
    return render(request, 'flow/contactus.html')


def faq_page(request):
    faqs = FAQ.objects.all()
    context = {'faqs': faqs}
    return render(request, "flow/faq.html", context)


def attractions_page(request):
    attractions = MajorAttractions.objects.all()
    context = {'major_attrs_slide': attractions}
    return render(request, 'flow/attractions.html', context)


def team_page(request):
    umbrellas = TeamCategory.objects.all()
    members = []
    for umbrella in umbrellas:
        members.append(TeamMember.objects.filter(team=umbrella))
    context = {'teams':umbrellas,'members':members}
    return render(request,"flow/teams.html",context)


def timeline(request):
    days = Timeline.objects.all()
    return render(request, 'flow/aarohan_timeline.html', {'days': days})


def timeline_detail(request, id):
    day = Timeline.objects.get(day_number=id)
    events = Events.objects.filter(
        eventDay__day_number__exact=id).order_by('date_time')
    context = {'day': day, 'events': events}
    return render(request, 'flow/event_timeline2.html', context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'flow/signin.html', {'msg': "Wrong Credentials"})
    else:
        return render(request, 'flow/signin.html', {'msg': None})


def judge_projects(request):
    context = {}
    context['msg'] = ""
    context['err'] = False
    if (not request.user.is_authenticated):
        return redirect('/')
    else:
        projects = TechmelaProject.objects.all()
        context['projects'] = projects
        if request.method == 'POST':
            m = request.POST['mark']
            f = request.POST['feas']
            t = request.POST['tech']
            project_id = request.POST['project']
            project = TechmelaProject.objects.get(id=project_id)
            review = Review(project=project, user=request.user,
                            mark=m, feas=f, tech=t)
            try:
                review.save()
                context["msg"] = "Saved last entry"
            except:
                context["msg"] = "Couldn't save last entry"
                context["err"] = True
        for idx, project in enumerate(context['projects']):
            review = Review.objects.all().filter(user=request.user, project=project)
            if len(review) == 0:
                setattr(context['projects'][idx], 'show', True)
            else:
                setattr(context['projects'][idx], 'show', False)
    return render(request, 'flow/projects.html', context)


def view_reviews(request):
    context = {}
    if request.user.is_authenticated:
        projects = TechmelaProject.objects.all()
        context["projects"] = projects
        for idx, project in enumerate(context["projects"]):
            reviews = Review.objects.all().filter(project=project)
            grand_total = 0
            avg_mark = 0
            avg_feas = 0
            avg_tech = 0
            for idy, review in enumerate(reviews):
                total = 0
                review_dict = model_to_dict(review)
                review_dict.pop('id')
                user_id = review_dict.pop('user')
                review_dict.pop('project')
                for k, v in review_dict.items():
                    total += int(v)
                    if k == "mark":
                        avg_mark += int(v)
                    elif k == "tech":
                        avg_tech += int(v)
                    else:
                        avg_feas += int(v)
                grand_total += total
                setattr(reviews[idy], "total", total)
                setattr(reviews[idy], "user", User.objects.get(id=user_id))
            setattr(context["projects"][idx], "reviews", reviews)
            setattr(context["projects"][idx], "grand_total", grand_total)
            lenx = len(reviews)
            if lenx == 0:
                lenx = 1
            setattr(context["projects"][idx], "avg_mark", avg_mark/lenx)
            setattr(context["projects"][idx], "avg_feas", avg_feas/lenx)
            setattr(context["projects"][idx], "avg_tech", avg_mark/lenx)
        print(context)
    return render(request, 'flow/reviews.html', context)


def techmela(request):
    robotics = TechmelaProject.objects.filter(domain="Robotics")
    assistive = TechmelaProject.objects.filter(domain="Assistive Technology")
    software = TechmelaProject.objects.filter(domain="Software Projects")

    return render(request, "flow/techmela.html", {'robotics': robotics, 'assistive': assistive, 'software' : software})

def aboutus(request):
    return render(request, "flow/comingsoon.html")

def timelineDay1(request):
     return render(request,"flow/aarohan_timeline.html")
def timelineDay2(request):
     return render(request,"flow/day2_timeline.html")
def timelineDay3(request):
    return render (request, "flow/day3_timeline.html")
def timelineDay4(request):
    return render (request, "flow/day4_timeline.html")


def merch(request):
    return render (request, "flow/merch.html")