import google.oauth2.credentials
import googleapiclient.discovery
import datetime

def add_google_calendar_event(command):
    credentials = google.oauth2.credentials.Credentials.from_authorized_user_file('credentials.json')
    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    event = {
        'summary': 'New Event',
        'start': {
            'dateTime': (datetime.datetime.now() + datetime.timedelta(hours=1)).isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': (datetime.datetime.now() + datetime.timedelta(hours=2)).isoformat(),
            'timeZone': 'America/Los_Angeles',
        }
    }
    service.events().insert(calendarId='primary', body=event).execute()
    return 'Event added to your calendar.'
