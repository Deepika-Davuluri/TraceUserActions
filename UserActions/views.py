from django.contrib.auth.models import User
from django.http import JsonResponse
import pytz

from UserActions.models import ActivityPeriod


def get_activity_periods_utc(request):
    response = {"ok": True, "members": []}
    is_utc = request.GET.get('utc', True)
    is_utc = False if is_utc == 'False' else True

    users = User.objects.all()
    users_info = []
    for user in users:
        user_info = {'id': user.id, 'real_name': user.username, 'tz': user.usertimezone.time_zone}
        activity_periods = get_user_activity_period(user, is_utc)
        user_info['activity_periods'] = activity_periods

        users_info.append(user_info)

    response['members'] = users_info
    return JsonResponse(response, safe=False)


def get_user_activity_period(user, utc=True):
    activity_periods = ActivityPeriod.objects.filter(user=user).order_by('start_time').values('start_time', 'end_time')

    if utc:
        for period in activity_periods:
            period['start_time'] = period['start_time'].strftime('%b %d %Y %H:%M%p')
            period['end_time'] = period['end_time'].strftime('%b %d %Y %H:%M%p')

    else:
        for period in activity_periods:
            to_tz = pytz.timezone(user.usertimezone.time_zone)
            start_time_localized = period['start_time'].replace(tzinfo=pytz.utc).astimezone(to_tz)
            end_time_localized = period['end_time'].replace(tzinfo=pytz.utc).astimezone(to_tz)

            period['start_time'] = start_time_localized.strftime('%b %d %Y %H:%M%p')
            period['end_time'] = end_time_localized.strftime('%b %d %Y %H:%M%p')

    return list(activity_periods)