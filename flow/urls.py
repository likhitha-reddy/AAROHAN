from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('home', home, name=""),
    path('events/<id>',events, name="category"),
    path('workshops',workshops, name="workshops"),
    path('faq',faq_page,name="faq"),
    path('aboutus',about_page,name="aboutus"),
    path('sponsors',sponsor_view,name="sponsors"),
    path('contactus',contactus,name="contactus"),
    path('attractions',attractions_page,name="attractions"),
    path('teams',team_page,name="teams"),
    path('timeline', timeline, name="timeline"),
    path('timeline/<id>', timeline_detail, name="timeline_detail")
]