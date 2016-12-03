import datetime
from rest_framework.renderers import JSONRenderer
from .models import Event


class AlertJSONRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        start_event = Event.objects.all().order_by('date')[0]
        end_event = Event.objects.all().order_by('-date')[0]
        data = {'start': datetime.datetime.utcfromtimestamp(start_event.date/1000).strftime('%Y%m/%d %H:%M:%S'),
                'end': datetime.datetime.utcfromtimestamp(end_event.date/1000).strftime('%Y/%m/%d %H:%M:%S'),
                'alerts': data}
        return super(AlertJSONRenderer, self).render(data, accepted_media_type, renderer_context)