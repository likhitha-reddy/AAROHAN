from django.contrib import admin
from .models import Events, EventCategory, Workshops, FAQ, About, Sponsors
# Register your models here.
admin.site.register(Events)
admin.site.register(EventCategory)
admin.site.register(Workshops)
admin.site.register(FAQ)
admin.site.register(About)
admin.site.register(Sponsors)