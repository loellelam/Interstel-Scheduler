from datetime import datetime
from datetime import timezone
import json

class ReadJson:
    def read_json():
        # open JSON file
        file = open('data.json')

        # return JSON object as a dictionary
        data = json.load(file)

        # for i in data:
        #     utc = i['utc']
        #     date = datetime.fromisoformat(utc[:-1]).astimezone(timezone.utc)
        #     # print(date)

        #     gs_id = i['gs-id']
        #     # print(gs_id)

        #     orb_event = i['orbital-event']
        #     # print(orb_event)

        #     if gs_id not in list:
        #         list.append(gs_id)

        # print list of gs ids
        # print(list)
        
        # close json file
        file.close()

        # # return list of gs ids
        # return list

        # # read in gs-id
        # # check if gs-id has been saved before or not
        # # if new gs-id, save as new one in list/vector idk(?)
        # # if not, bring up saved gs-id from list/vector(?)

        # # finding length of time: find where each AOS0 starts
    
    def getEventName(list):
        # open JSON file
        file = open('data.json')

        # return JSON object as a dictionary
        data = json.load(file)

        # iterate through JSON file
        for i in data:
                # read in event name
                event_name = i['event_name']
                # save elements of event name in list
                name = event_name.split("_", 1)

                if (name[0] != "UMBRAIN" and name[0] != "UMBRAOUT"):
                    # check if new event name
                    # if new, add to list
                    if name[1] not in list:
                        list.append(name[1])

        # print list of event names
        # print(list)

        # close JSON file
        file.close()

        # return list of event names
        return list

    def getUtc():
        return