from django.db import models

# Create your models here.
class EventCategory(models.Model):
    groupName = models.CharField(max_length = 255,unique=True, help_text="Name of the event group")
    groupId = models.CharField(max_length = 20,unique=True, help_text="ID by which group will be identified")
    logo = models.ImageField(blank=True)

    def __str__(self):
        return self.groupName

class Events(models.Model):
    eventGroup = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    eventName = models.CharField(max_length=50, unique=True, help_text="Enter the name of the event")
    eventId = models.CharField(max_length=50,help_text="Enter the ID of the event")
    logo = models.ImageField(blank=True)
    description = models.TextField(help_text="Enter short description of the event")
    problem_statement = models.TextField(help_text="Enter the problem statement of the event here")
    date_time = models.DateTimeField()
    venue = models.CharField(max_length=50,null=False)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.eventName

class Workshops(models.Model):
    workshopName = models.CharField(max_length=100,unique=True, help_text="Enter name of workshop")
    workshopId = models.CharField(max_length=50, help_text="Enter the ID of the workshop")
    logo = models.ImageField(blank=True)
    description = models.TextField(help_text="Enter short description of the workshop")
    date_time = models.DateTimeField()
    venue = models.CharField(max_length=50, null=False)
    resgistration_open = models.BooleanField(default=True)

    def __str__(self):
        return self.workshopName

class Sponsors(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=True)
    url = models.EmailField(help_text='URL of the sponsor')
    
    def __str__(self):
        return self.name 

class About(models.Model):
    text = models.TextField(help_text="Enter the about page of the fest here")
    logo = models.ImageField(blank=True)
    identifier = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.identifier

class FAQ(models.Model):
    identifier = models.CharField(max_length = 50)
    question = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.identifier

class MajorAttractions(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(help_text="Enter the description of the attraction here")
    logo = models.ImageField(blank = True)

    def __str__(self):
        return self.name

class TeamCategory(models.Model):
    name = models.CharField(max_length = 100, blank = False, help_text="Enter name of the team category here")
    teamId = models.CharField(max_length = 50, unique=True, help_text="Enter category ID")
    def __str__(self):
        return self.name

class TeamMember(models.Model):
    team = models.ManyToManyField(TeamCategory)
    name = models.CharField(max_length=50, unique=True, help_text="Enter the name of the member here")
    position = models.CharField(max_length=50, help_text="Enter the position of the person")
    profile_img = models.ImageField()
    club_choice = (
        ("GLUG","GNU/Linux Users' Group"),
        ("CCA","Centre for Cognitive Activities"),
        ("SAE","SAE"),
        ("MNTC","Maths n Tech Club"),
        ("REC","RECursion"),
    )
    choice = models.CharField(
        max_length=5,
        choices= club_choice,
        default="GLUG"
    )

    def __str__(self):
        return self.name

