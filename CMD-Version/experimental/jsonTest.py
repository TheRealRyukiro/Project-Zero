import json
userData = None
Player = None
Enemy = None
try: 
    jsonFile = open("experimental/data.json", "r")
    userData = json.loads(jsonFile.read())
except OSError:
    print("cannot open file")
else:
    print("File Opened Successfully & Data Transferred.")
    jsonFile.close()

Player = userData["Player"]
print(Player["Name"])