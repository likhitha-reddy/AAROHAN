from django.shortcuts import render, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.forms.models import model_to_dict
from django.contrib.auth.models import User

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
            review = Review(project=project, user=request.user, mark=m, feas=f, tech=t)
            try:
                review.save()
                context["msg"] = "Saved last entry"
            except:
                context["msg"] = "Couldn't save last entry"
                context["err"] = True
        for idx, project in enumerate(context['projects']):
            review = Review.objects.all().filter(user=request.user, project=project)
            if len(review) is 0:
                setattr(context['projects'][idx], 'show', True)
            else:
                setattr(context['projects'][idx], 'show', False)
    return render(request, 'flow/projects.html', context)

def view_reviews(request):
    context = {}
    if request.user.is_authenticated:
        projects = TechmelaProject.objects.all()
        context["projects"] = projects
        for idx,project in enumerate(context["projects"]):
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
