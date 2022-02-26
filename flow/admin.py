from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Events)
admin.site.register(Workshops)
admin.site.register(FAQ)
admin.site.register(About)
admin.site.register(Sponsors)
admin.site.register(TeamCategory)
admin.site.register(TeamMember)
admin.site.register(MajorAttractions)
admin.site.register(Timeline)
admin.site.register(TechmelaProject)
admin.site.register(Review)
admin.site.register(Arena)

#Social Initiatives
class SocialInitiativesPhotosAdmin(admin.StackedInline):
    model = SocialInitiativesPhotos

class SocialInitiativesAdmin(admin.ModelAdmin):
    inlines = [SocialInitiativesPhotosAdmin]
    list_display = ('name',)
admin.site.register(SocialInitiatives , SocialInitiativesAdmin)

#Industrial Visits
class IndustrialVisitsPhotosAdmin(admin.StackedInline):
    model = IndustrialVisitsPhotos

class IndustrialVisitsAdmin(admin.ModelAdmin):
    inlines = [IndustrialVisitsPhotosAdmin]
    list_display = ('name',)
admin.site.register(IndustrialVisits , IndustrialVisitsAdmin)