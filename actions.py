from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import requests
import json

API_URL = "http://indianrailapi.com/api/v2/livetrainstatus/apikey/"
API_KEY = ""

from datetime import date
today = date.today()
DATE = today.strftime("%Y%m%d")

class ActionStatus(Action):
    def name(self):
        return 'action_status'
    
    def run(self, dispatcher, tracker, domain):
        TRAIN = tracker.get_slot('train_number')
        complete_url = API_URL + APIKEY + "/trainnumber/" + TRAIN + "/date/" + DATE + "/"
        response = requests.get(complete_url)
        result = response.json()
        if result["ResponseCode"] == 200:
            y = result["TrainRoute"]
            source_station = y[0]["StationName"]
            destination_station = y[len(y)-1]["StationName"]
            out = "Train number: {}\nSource Station: {}\nDestination Station: {}\n".format(TRAIN, source_station, destination_station)
            dispatcher.utter_message(out)
        return [SlotSet('train_number',TRAIN)]

