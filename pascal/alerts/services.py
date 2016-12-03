import datetime
from collections import deque

import requests

from .models import Event, Alert


def get_events():
    # url = 'http://127.0.0.1:8080/events.json'
    url = 'https://sample-api.pascalmetrics.com/api/events'
    params = {'api-key': 'nu11p0int3r!'}
    r = requests.get(url, params=params)
    return r.json()


def insert_events(events):
    insert_transaction = []
    for event in events:
        m_event = Event()
        m_event.date = event['date']
        m_event.name = event['name']
        m_event.value = event['value']
        insert_transaction.append(m_event)
    Event.objects.bulk_create(insert_transaction)


def alert_checker(events):
    # name = {'lab one': [[timestamps],[values]]}
    names = {}
    insert_transaction = []
    for event in events:
        if event.name in names:
            names[event.name][0].append(event.date)
            names[event.name][1].append(event.value)
            # Greater than 24 hours
            while names[event.name][0][-1] - names[event.name][0][0] > 1000 * 60 * 60 * 24:
                names[event.name][0].popleft()
                names[event.name][1].popleft()
            # New Alert
            if sum(names[event.name][1]) > 2000:
                m_alert = Alert()
                m_alert.timestamp = datetime.datetime.utcfromtimestamp(event.date/1000).strftime('%Y/%m/%d %H:%M:%S')
                m_alert.name = event.name
                m_alert.value = sum(names[event.name][1])
                insert_transaction.append(m_alert)
        else:
            names[event.name] = [deque([event.date]), deque([event.value])]
    Alert.objects.bulk_create(insert_transaction)