from django.urls import path


from . import views 
from Eventia_web.urls import urlpatterns


urlpatterns = [
    path("register_for_event" ,views.register_for_event, name="register_for_event"  ),
    path("event_register" ,views.events_register, name="event_register")
    
]