from calendar_app import api
from calendar_app.controllers.events_controller import Addevent, Updateevent, Deleteevent
api.add_resource(Addevent, '/api/v1/calendars/<calendarId>/events')
api.add_resource(Updateevent, '/api/v1/calendars/<calendarId>/events/<eventId>')
api.add_resource(Deleteevent, '/api/v1/calendars/<calendarId>/events/<eventId>')