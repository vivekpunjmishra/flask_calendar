import bcrypt as bcrypt
from calendar_app import db
from datetime import datetime

class EventsModel(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    # eventId = db.Column(db.Integer)
    summary = db.Column(db.String(120))
    description = db.Column(db.String(120))
    start_dateTime = db.Column(db.DateTime, default=datetime.utcnow())
    end_dateTime = db.Column(db.DateTime, default=datetime.utcnow())
    timeZone = db.Column(db.String(120))
    colorId = db.Column(db.String(255))
    status = db.Column(db.String(120))
    transparency = db.Column(db.String(120))
    visibility = db.Column(db.String(255), default= 'private')
    location = db.Column(db.Text)
    attachments = db.Column(db.Boolean, default=True)
    fileUrl = db.Column(db.String(255))
    title = db.Column(db.String(120))
    attendees = db.Column(db.Integer)
    displayName = db.Column(db.DateTime, default=datetime.utcnow())
    comment = db.Column(db.String(8))
    email = db.Column(db.String(20),unique=True)
    optional = db.Column(db.Boolean, default=False)
    orgnizer = db.Column(db.Boolean, default=True)
    responseStatus = db.Column(db.String(120))
    recurrence = db.Column(db.Integer)
    maxAttendees = db.Column(db.String(120))
    sendNotification = db.Column(db.Boolean, default=True)
    sendUpdate = db.Column(db.String(255), default= 'private')
    supportsAttachement = db.Column(db.Boolean, default=True)

    # access_token = db.Column(db.Text)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete()
        db.session.commit()