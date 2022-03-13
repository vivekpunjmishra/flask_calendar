from datetime import datetime, date, timedelta
from pprint import pprint
from urllib import response
from calendar_app.models.events_model import EventsModel
from calendar_app.helper.Google import convert_to_RFC_datetime, create_service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

colors = service.colors().get().execute()
recurrence = [
    'RRULE:FREQ=MONTHLY;COUNT=2'
]

hour_adjustment = -8


class EventService:

    def insert_events(self, calendarId, summary, location, description,
                        start, end, recurrence, attendees, reminders, conferenceData):

        print("!!!!!!!!!!!!!!!!!!!",calendarId)
        response = service.events().insert(
            calendarId=calendarId,
            summary=summary,
            location=location,
            description=description,
            start=start,
            end=end,
            recurrence=recurrence,
            attendees=attendees,
            reminders=reminders,
            conferenceData=conferenceData
            ).execute()
        print(response)
        events = EventsModel(calendarId=calendarId, summary=summary,location=location,description=description, start=start,
                    end=end,recurrence=recurrence,attendees=attendees,
                    reminders=reminders,conferenceData=conferenceData)
        print(response)
        events.save()  
        # eventId = response['Id']          

    def update_events(Calendar_id, eventId, startdateTime, enddateTime, summary, description):
        response['start']['dateTime'] = startdateTime
        response['end']['dateTime'] = enddateTime
        response['summary'] = summary
        response['description'] = description
        service.events().update(calendarId=Calendar_id,
            eventId =eventId,
            body = response).execute()  

    def delete_events(Calendar_id, eventId): 
        service.events().delete(calendarId=Calendar_id, eventId = eventId).execute()         