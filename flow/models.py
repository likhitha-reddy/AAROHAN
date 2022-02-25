from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Timeline(models.Model):
    day_number = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    body = models.TextField()
    image = models.ImageField(blank=True, upload_to="day_img/")


class Events(models.Model):
    eventDay = models.ForeignKey(Timeline, on_delete=models.DO_NOTHING)
    eventName = models.CharField(
        max_length=50, unique=True, help_text="Enter the name of the event")
    eventId = models.CharField(
        max_length=50, help_text="Enter the ID of the event")
    logo = models.ImageField(blank=True, upload_to="event_images/")
    description = models.TextField(
        help_text="Enter short description of the event")
    date_time = models.DateTimeField()
    venue = models.CharField(max_length=50, null=False, blank=True)
    registration_link = models.CharField(
        max_length=1024, blank=True, help_text="Enter the registration link here")
    event_link = models.CharField(
        max_length=1024, blank=True, help_text="If there is no registration, then website link")

    def __str__(self):
        return self.eventName


class Workshops(models.Model):
    workshopName = models.CharField(
        max_length=100, unique=True, help_text="Enter name of workshop")
    workshopId = models.CharField(
        max_length=50, help_text="Enter the ID of the workshop")
    logo = models.ImageField(blank=True, upload_to="workshop_images/")
    description = models.TextField(
        help_text="Enter short description of the workshop")
    date_time = models.DateTimeField()
    venue = models.CharField(max_length=50, null=False)
    contact = models.CharField(max_length=50)
    registration_open = models.BooleanField(default=True)
    registration_link = models.CharField(
        max_length=1024, blank=True, help_text="Enter the registration link here")

    def __str__(self):
        return self.workshopName

class SocialInitiatives(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    date_time = models.DateTimeField(null=True)
    webinar_link = models.CharField(max_length=1024, blank=True, null=True)
    app_link = models.CharField(max_length=1024, blank=True, null=True)
    poster = models.ImageField(blank=True, null=True, upload_to="social_images/")

class IndustrialVisits(models.Model):
    name = models.CharField(max_length=250, unique=True)
    image = models.ImageField(blank=True, null=True, upload_to="industrial_images/")
    video_link = models.CharField(max_length=1024, blank=True, null=True)


class SocialInitiativesPhotos(models.Model):
    social_name = models.ForeignKey(SocialInitiatives, on_delete=models.CASCADE, related_name="socialImages")
    image = models.ImageField(blank=True, null=True, upload_to="social_images/")


class Sponsors(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to="sponsors/")
    url = models.EmailField(help_text='URL of the sponsor', blank=True)

    def __str__(self):
        return self.name


class About(models.Model):
    text = models.TextField(help_text="Enter the about page of the fest here")
    logo = models.ImageField(blank=True)
    identifier = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.identifier


class FAQ(models.Model):
    identifier = models.CharField(max_length=50)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.identifier


class MajorAttractions(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(
        help_text="Enter the description of the attraction here")
    image = models.ImageField(blank=True, upload_to="mjr_attrs/")
    url = models.CharField(max_length=1024, blank=True,
                           help_text='URL of major attractions')

    def __str__(self):
        return self.name


class TeamCategory(models.Model):
    name = models.CharField(max_length=100, blank=False,
                            help_text="Enter name of the team category here")
    teamId = models.CharField(
        max_length=50, unique=True, help_text="Enter category ID")
    team_image = models.ImageField(blank=True, upload_to="team_images/")

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    team = models.ManyToManyField(TeamCategory)
    name = models.CharField(max_length=50,
                            help_text="Enter the name of the member here")
    position = models.CharField(
        max_length=50, help_text="Enter the position of the person", blank=True)
    profile_img = models.ImageField(blank=True, upload_to="members/")
    club_choice = (
        ("GLUG", "GNU/Linux Users' Group"),
        ("CCA", "Centre for Cognitive Activities"),
        ("SAE", "SAE"),
        ("MNTC", "Maths n Tech Club"),
        ("REC", "RECursion"),
    )
    choice = models.CharField(
        max_length=5,
        choices=club_choice,
        default="GLUG"
    )

    def __str__(self):
        return self.name


class TechmelaProject(models.Model):
    title = models.CharField(max_length=30, default="Title here")
    team_name = models.CharField(max_length=20)
    description = models.TextField(default="Description here")
    pdf_link = models.URLField(
        default="https://drive.google.com/file/d/0B1HXnM1lBuoqMzVhZjcwNTAtZWI5OS00ZDg3LWEyMzktNzZmYWY2Y2NhNWQx/preview")
    video_link = models.URLField(
        default="https://drive.google.com/file/d/1KFFhLqRLhdF27KwVVe0npoVX0lNLPhpM/preview")
    project_domain_choice = (
        ('Robotics', 'Robotics'),
        ('Assistive Technology', 'Assistive Technology'),
        ('Software Projects', 'Software Projects'),
    )
    domain = models.CharField(
        max_length=30, choices=project_domain_choice, default='Robotics')
    project_image = models.ImageField(
        upload_to="techmela_projects/", null=True, blank=True)

    def __str__(self):
        return (self.title + " by Team:" + self.team_name)


class Review(models.Model):
    project = models.ForeignKey(TechmelaProject, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    feas = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    tech = models.PositiveIntegerField(
        default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])

    def __str__(self):
        return ("Review of " + self.project.name + " by " + self.user.username)


class Arena(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(
        blank=True, help_text="Enter the description of the attraction here")
    logo = models.ImageField(blank=True, upload_to="arena/")
    url = models.CharField(max_length=100, blank=True,
                           help_text='URL of Arena item')

    def __str__(self):
        return self.description
