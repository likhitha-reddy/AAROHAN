from django.urls import path
from .views import index, eventGroups, events, workshops


urlpatterns = [
    path('', index, name="home"),
    path('categories',eventGroups, name="categories"),
    path('category/<id>',events, name="category"),
    path('workshops',workshops, name="workshops")
]