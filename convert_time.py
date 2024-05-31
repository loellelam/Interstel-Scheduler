from datetime import datetime
from datetime import timezone
import json

# open JSON file
file = open('data.json')

# return JSON object as a dictionary
data = json.load(file)

for i in data:
    utc = i['utc']
    date = datetime.fromisoformat(utc[:-1]).astimezone(timezone.utc)
    print(date)

# datetime.fromisoformat()
 
file.close()