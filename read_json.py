from datetime import datetime
from datetime import timezone
from collections import namedtuple
import json

class Event:
    def __init__(self):
        self.event_flag = -1
        self.event_name = ""
        self.event_type = -1
        self.event_utc = -1
        self.start_time = -1
        self.end_time = -1
        self.max_time = -1

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

        # Convert all MJD to unix time
        for i, event in enumerate(cls.data):
            mjd = event["event_utc"]  
            unix = (mjd - 40587) * 86400
            cls.data[i]["event_utc"] = float(unix)

    @classmethod
    def get_start_utc(cls):
        min = float('inf')
        for event in cls.data:
            if (event["event_utc"] < min):
                min = event["event_utc"]
        min = 1686474321.0012758 # TEMPORARILY USED FOR TESTING
        return min
    
    @classmethod
    def get_end_utc(cls):
        max = float('-inf')
        for event in cls.data:
            if (event["event_utc"] > max):
                max = event["event_utc"]
        return max
    
    @classmethod
    def getEventName(cls):
        list = []
        # iterate through JSON file
        for i in cls.data:
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
        print(list)

        # return list of event names
        return list
    
    # find aos/los pairs
    def findPairs():
        # initialize list to hold aos/los pairs
        pairs = []

        # define named tuple to hold the events
        Event = namedtuple('Event', ['name', 'AOS', 'MAX', 'LOS'])

        # open JSON file
        file = open('data.json')

        # return JSON object as a dictionary
        data = json.load(file)

        # iterate through JSON file
        # find pairs (umbra in, umbra out)/(aos, los)
        for i in data:
            # read in event name
            event_name = i['event_name']

            # look for starting aos
            if'AOS' in event_name:
                print("AOS: " + event_name)

                # find and save location of event
                name = event_name.split("_", 1)
                name = name[1]
                print("AOS name: " + name)

                # create new event and save it's AOS
                E = Event(name, i['event_utc'], None, None)
                # add event into pairs list
                pairs.append(E)
                print(E)
                print()

            # look for ending los
            if 'LOS' in event_name:
                # find and save location of event
                name = event_name.split("_", 1)
                name = name[1]
                print("LOS name: " + name)

                for index, event in enumerate(pairs):
                    if event.name == name and event.LOS is None:
                        pairs[index] = event._replace(LOS = i['event_utc'])
                        print(pairs[index])
                        break

                print()
                # print("LOS: " + event_name)

            # look for max
            if 'MAX' in event_name:
                print()
                # print("MAX: " + event_name)

            # once aos found, find the event name

        # create named tuples for events

        # find umbra pairs

        print(pairs)

        # close JSON file
        file.close()

        # return list of aos/los pairs
        return pairs
    
    # from loelle's work
    @classmethod
    def get_event_utc(cls):
        for i, event in enumerate(cls.data):
            mjd = event["event_utc"]  
            unix = mjd - 40587 * 86400
            cls.data[i]["event_utc"] = int(unix)
                    
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
