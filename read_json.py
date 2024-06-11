from datetime import datetime
from datetime import timezone
import json

def read_json():
    # open JSON file
    file = open('data.json')

    # return JSON object as a dictionary
    data = json.load(file)

    # create empty list to hold gs ids
    list = []

    for i in data:
        utc = i['utc']
        date = datetime.fromisoformat(utc[:-1]).astimezone(timezone.utc)
        # print(date)

        gs_id = i['gs-id']
        # print(gs_id)

        orb_event = i['orbital-event']
        # print(orb_event)

        if gs_id not in list:
            list.append(gs_id)

        # print()

    print(list)

    # datetime.fromisoformat()
    
    file.close()

    # read in gs-id
    # check if gs-id has been saved before or not
    # if new gs-id, save as new one in list/vector idk(?)
    # if not, bring up saved gs-id from list/vector(?)

    # finding length of time: find where each AOS0 starts
