from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import random

TIMEZONE_CHOICES = (('Asia/Kolkata', 'Asia/Kolkata'), ('America/Los_Angeles', 'America/Los_Angeles'),
                    ('Africa/Algiers', 'Africa/Algiers'), ('AU', 'Australia/Sydney'))


class UserTimeZone(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    time_zone = models.CharField(max_length=50, choices=TIMEZONE_CHOICES, default='IN')


@receiver(post_save, sender=User)
def create_user_timezone(sender, instance, created, **kwargs):
    if created:
        UserTimeZone.objects.create(user=instance, time_zone=random.choices(['Asia/Kolkata',
                                                    'America/Los_Angeles', 'Australia/Sydney', 'Africa/Algiers'])[0])


@receiver(post_save, sender=User)
def save_user_timezone(sender, instance, **kwargs):
    instance.usertimezone.save()


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(blank=True)
    end_time = models.DateTimeField(blank=True)
