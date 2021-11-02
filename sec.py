import json

x = json.load(open("sprite2/clsys.json"))
print(x["rockets"].__len__())