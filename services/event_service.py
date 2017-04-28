import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId

import ast
from models import model
from flask import jsonify
import json

client = MongoClient('localhost', 27017)
db = client.Kiwanis


def list_events():
    collection = db.Event
    events = []
    for event in collection.find():
        e = dumps(event)
        _event = ast.literal_eval(e)
        current_event = model.Event()
        for key, value in _event.iteritems():
            if key == 'Name':
                current_event.set_name(value)
            elif key == 'Address':
                current_event.set_address(value)
            elif key == 'Address2':
                current_event.set_address2(value)
            elif key == 'Coordinator':
                current_event.set_coordinator(value)
            elif key == 'Date':
                current_event.set_date(value)
            elif key == 'Image':
                current_event.set_image(value)
            elif key == 'Description':
                current_event.set_description(value)
            elif key == '_id':
                for k,v in value.iteritems():
                    current_event.set_id(v)
        events.append(current_event.dictify())

    return events


def create_event(data):
    collection = db.Event
    event = create_event_model(data)
    try:
        collection.insert_one(event.dictify())
        message = {
            "Status": "Ok"
        }
        code = 1
    except Exception as e:
        print(e)
        message = {
            "Status": "An Error Occurred: " + str(e)
        }
        code = 2

    return code, message


def update_event(json):
    e = create_event_model(json)

    db.Event.update(
        {"_id": ObjectId(e.id)},
        e.dictify(),
        upsert=True
    )


def create_event_model(data):
    e = model.Event()
    e.set_name(data["Name"])
    e.set_address(data["Address"])
    e.set_address2(data["Address2"])
    e.set_image(data["Image"])
    e.set_description(data["Description"])
    e.set_coordinator(data["Coordinator"])
    e.set_date(data["Date"])
    e.set_id(data["id"])
    return e