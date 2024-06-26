from datetime import datetime
from datetime import timezone
import json

class ReadJson:
    data = []

    @classmethod
    def read_json(cls):
        # open JSON file
        file = open('data.json')

        # return JSON object as a dictionary
        cls.data = json.load(file)

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

        # # print list of gs ids
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

        # Convert all MJD to unix time
        for i, event in enumerate(cls.data):
            mjd = event["event_utc"]  
            unix = (mjd - 40587) * 86400
            cls.data[i]["event_utc"] = float(unix)
    
    @classmethod
    def getEventName():
        return        

    @classmethod
    def get_start_utc(cls):
        min = float('inf')
        for event in cls.data:
            if (event["event_utc"] < min):
                min = event["event_utc"]
        return min
    
    @classmethod
    def get_end_utc(cls):
        max = float('-inf')
        for event in cls.data:
            if (event["event_utc"] > max):
                max = event["event_utc"]
        return max
    
    @classmethod
    def get_umbra_utc(cls):
        umbra = {
            "in": [],
            "out": []
        }

        for event in cls.data:
            if (event["event_name"] == "UMBRAIN"):
                umbra["in"].append(event["event_utc"])
            if (event["event_name"] == "UMBRAOUT"):
                umbra["out"].append(event["event_utc"])

        return umbra
