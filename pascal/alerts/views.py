from rest_framework.views import APIView
from rest_framework.response import Response

from .renderer import AlertJSONRenderer
from . import services
from .models import Alert, Event
from .serializer import AlertSerializer


# Create your views here.
class LabAlerts(APIView):
    renderer_classes = (AlertJSONRenderer,)

    def get(self, request):
        # Wipe API data
        # This is bad and shouldn't be done, but for making something quick and dirty it works
        Event.objects.all().delete()
        Alert.objects.all().delete()
        # Get api data
        # Put api data in model
        services.insert_events(services.get_events())
        # calculate out if alert exists
        events = Event.objects.all().order_by('date')
        services.alert_checker(events)

        # Output Data
        alert = Alert.objects.all()
        serialized_alerts = AlertSerializer(alert, many=True)
        return Response(serialized_alerts.data)

    def post(self):
        pass
