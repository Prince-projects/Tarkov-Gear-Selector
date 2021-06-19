import os
import glarkov
import json

email = ""
password = ""

t = glarkov.tarkov.Tarkov(email, password)

f = open("testing_get_all_items.txt", "w+")
f.write(json.dumps(t.get_items(), indent=4))
f.close()
import message
print(message.Label)
# Get items, sort them by name only, get each item name, update dict.