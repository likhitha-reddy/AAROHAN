from django.urls import path
from .views import index, eventGroups, events


urlpatterns = [
    path('', index, name="home"),
    path('categories',eventGroups, name="categories"),
    path('categories/<slug:gId>',events, name='category')
]