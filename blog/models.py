from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # models.ForeignKey - NEEDS WORK AND MORE UNDERSTADNING
    # https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ForeignKey.on_delete
    title = models.CharField(max_length=200)
    # models.CharField - This is how a text is defined with a limited number of characters
    text = models.TextField()
    # models.TextField - This is for long text without a limit. Ideal for blog post contents.
    created_date = models.DateTimeField(default=timezone.now)
    # models.DateTimeField - This is for a Date and Time.
    published_date = models.DateTimeField(blank=True, null=True)
    # "null=True" will store blank values as NULL in the DB. Default of Null is False
    # "blank" determins if a field is required in forms, including admin and custom forms
    # "blank=True" means that field is not required.
    # "blank=Flase" means that the field cannot be blank.
    # "blank=True, null=True" is used frequently as when we allow a field to be blank in form, DB is needed to be NULL

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        # str.title() allows the string to be converted into lowercase except for the first letter.
        # str = "this is string example....wow!!!";
        # print str.title()
        # This Is String Example....Wow!!!
