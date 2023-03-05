from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('home', home, name=""),
    # path('events/<id>', events, name="category"),
    path(
        "social-initiatives",
        socialInitiative_view,
        name="socialInitiatives",
    ),
    path(
        "industrial-visits",
        industrialvisit_view,
        name="industrialvisits",
    ),
    # path('workshops', workshops, name="workshops"),
    # path('events/<id>',events, name="category"),
    path('workshops',workshops, name="workshops"),
    path('faq',faq_page,name="faq"),
    path('aboutus',about_page,name="aboutus"),
    path('sponsors',sponsor_view,name="sponsors"),
    path('contactus',contactus,name="contactus"),
    path('attractions',attractions_page,name="attractions"),
    path('teams/',team_page,name="teams"),
    path('events', events, name="events"),
    path('timeline', timeline, name="timeline"),
    path('judge-auth', signin, name="signin"),
    path('judgeprojects', judge_projects, name="judgeprojects"),
    path('projectreviews', view_reviews, name="projectreviews"),
    path('techmela', techmela, name="techmela"),

    path('timeline_day1',timelineDay1,name="timelineDay1"),
    path('timeline_day2',timelineDay2,name="timelineDay2"),
    path('timeline_day3',timelineDay3,name="timelineDay3"),
    path('timeline_day4',timelineDay4,name="timelineDay4"),

    path('buymerch',merch,name="merch"),
]