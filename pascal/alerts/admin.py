from django.contrib import admin
from .models import Alert, Event

# Register your models here.

admin.site.register(Alert)
admin.site.register(Event)