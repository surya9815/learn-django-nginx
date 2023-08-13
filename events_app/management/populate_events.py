import datetime
import random
from lorem import paragraph

from django.core.management.base import BaseCommand

from events_app.models import Event

class Command(BaseCommand):
    
    @staticmethod
    def create_events():
        number_of_events = random.randrange(10000)