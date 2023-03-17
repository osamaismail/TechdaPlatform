from django.db import models
from django.contrib.auth.models import User
import uuid
from tinymce import models as tinymce_models


ACTIVITY_LIST = (('0', 'Lecture'),
                 ('1', 'Workshop'),
                 ('3', 'Conference'),
                 ('4', 'Thon'),
                 )

PLACE_LIST = (('0', 'Online'),
              ('1', 'Local'),
              )

class Activity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructor')
    actType = models.CharField(max_length=1, choices=ACTIVITY_LIST, default='0')
    title = models.CharField(max_length=150, null=True, blank=False)
    actImage = models.ImageField('Event Image', upload_to='event/')
    content = tinymce_models.HTMLField(null=True)
    place = models.CharField(max_length=1, choices=PLACE_LIST, default='0')
    location = tinymce_models.HTMLField(null=True)
    statusEnd = models.BooleanField(default=False)
    actDate = models.DateField(null=True)
    actTime = models.TimeField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.title


class Attend(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attend')
    confirm = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=True)

    def __str__(self):
        return self.activity.title


class Volunteer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, blank=False, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='volunteer')
    accepted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=True)

    def __str__(self):
        return self.activity.title