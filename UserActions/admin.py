from django.contrib import admin

# Register your models here.
from UserActions.models import *

admin.site.register(UserTimeZone)
admin.site.register(ActivityPeriod)
