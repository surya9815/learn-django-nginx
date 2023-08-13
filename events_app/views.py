from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.views.generic import ListView,DetailView

from events_app.models import Event

class EventDetailsView(DetailView):
    models = Event
    template_name = 'event_details.html'
    context_object_name = 'event'

class EventsListView(ListView):
    model = Event
    template_name = 'events_list.html'
    context_object_name = 'events'

    paginate_by = 100
    ordering = 'date'

    def get_context_data(self,object_list=None ,**kwargs):
        context = super(EventsListView, self).get_context_data()
                # timeit.timeit(lambda: "-".join(map(str, range(1000))), number=100)
        # context['REDIS_CACHED_TIME'] = settings.REDIS_CACHED_TIME
        return context

