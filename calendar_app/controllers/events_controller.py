from flask_restful import Resource, reqparse
from sqlalchemy import delete
from calendar_app import app
from calendar_app.services.service import EventService


"""
Create an event
"""
class Addevent(Resource):
    def post(self, calendarId):
        # try:
            parser = reqparse.RequestParser()
            parser.add_argument('summary', type=str)
            parser.add_argument('location', type=str)
            parser.add_argument('description', type=str)
            parser.add_argument('start', type=dict, help='start can not be blank', required=True)
            parser.add_argument('end', type=dict, help='end can not be blank', required=True)
            parser.add_argument('recurrence', type=str)
            parser.add_argument('attendees', type=dict)
            parser.add_argument('reminders', type=dict)
            parser.add_argument('conferenceData', type=dict)
            args = parser.parse_args()
            print("RRRRRRRRRRR",args['conferenceData'])
            app.logger.info("calendar:events::post::params::{}".format(args))
            if calendarId:
                app.logger.info("Client:Projects::post:user_id:{}".format(calendarId))
                return EventService().insert_events(calendarId, args['summary'],args['location'],
                                                    args['description'],args['start'],args['end'],
                                                    args['recurrence'],args['attendees'],
                                                    args['reminders'],args['conferenceData'])
            else:
                return {'err': 'CalendarId is Not Found!!', 'status': 0}, 401

        # except Exception as e:
        #     app.logger.error("Client:BusinessProfile:post:: {}".format(e))
        #     return {'err': str(e), 'status': 0, 'data': {}}, 500
"""
Update an event
"""
class Updateevent(Resource):
    def put(self):
        # try: 
            parser = reqparse.RequestParser()
            parser.add_argument('Calendar_id', type=str, help='Calendar_id can not be blank', required=True)
            parser.add_argument('eventId', type=str, help='eventId can not be blank', required=True)
            parser.add_argument('startdateTime', type=str, help='startdateTime can not be blank', required=True)
            parser.add_argument('enddateTime', type=str, help='enddateTime can not be blank', required=True)
            parser.add_argument('summary', type=str, help='summary can not be blank', required=True)
            parser.add_argument('description', type=str, help='description can not be blank', required=True)

            args = parser.parse_args()
            print(args)
            app.logger.debug("Calendar:events::post::params::{}".format(args))
            return EventService().update_events(args['startdateTime'],args['enddateTime'],args['summary'],args['description'])
        # except Exception as e:
        #     app.logger.error("Users:CustomLogin:post:: {}".format(e))
        #     return {'err': 'Something went wrong', 'status': 0, 'data': {}}, 500

"""
Delete an event
"""
class Deleteevent(Resource):
    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('Calendar_id', type=str, help='Calendar_id can not be blank', required=True)
            parser.add_argument('eventId', type=str, help='eventId can not be blank', required=True)
            args = parser.parse_args()
            app.logger.debug("Calendar:events::post::params::{}".format(args))
            return EventService().delete_events(args['Calendar_id'],args['eventId'])
        except Exception as e:
            app.logger.error("Users:CustomLogin:post:: {}".format(e))
            return {'err': 'Something went wrong', 'status': 0, 'data': {}}, 500        