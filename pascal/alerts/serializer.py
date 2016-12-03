from rest_framework import serializers
from .models import Alert, AlertResponse


class AlertSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alert
        fields = ('timestamp', 'name', 'value')


