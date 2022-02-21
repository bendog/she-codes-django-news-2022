from urllib import parse
from zoneinfo import ZoneInfo

from django.conf import settings
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


class TimezoneMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # get timezone name from browser cookie
        tz_name = request.COOKIES.get('timezone') or settings.TIME_ZONE
        if tz_name:
            # if tz_name is set, activate the timezone
            timezone.activate(ZoneInfo(parse.unquote(tz_name)))
        else:
            timezone.deactivate()
        return self.get_response(request)
