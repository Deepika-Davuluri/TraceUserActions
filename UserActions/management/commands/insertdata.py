from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random, datetime

from UserActions.models import ActivityPeriod


class Command(BaseCommand):

    def handle(self, *args, **options):
        for i in range(1, 11):
            user_name = 'user_' + str(i)
            User.objects.create_user(user_name, password='Welcome@2020')

        users = User.objects.all()
        for i in range(0, 3):
            month = random.choice([1, 2, 3, 4, 5])
            year = random.choice([2019, 2020])
            day = random.randint(1, 30)
            start_date = datetime.date(year, month, day)
            for user in users:
                hour = random.randint(0, 23)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                tm = datetime.time(hour, minute, second)
                start_dttm = datetime.datetime.combine(start_date, tm)
                end_dttm = start_dttm + datetime.timedelta(hours=random.randint(1, 4))
                ActivityPeriod.objects.create(user=user, start_time=start_dttm, end_time=end_dttm)
