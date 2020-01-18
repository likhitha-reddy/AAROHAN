from django.contrib import admin
from .models import Events, EventCategory, Workshops
# Register your models here.
admin.site.register(Events)
admin.site.register(EventCategory)
admin.site.register(Workshops)