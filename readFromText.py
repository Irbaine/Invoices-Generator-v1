file = open('myInfo.txt', 'r')
read = file.readlines()
modified = []

for line in read:
    modified.append(line.strip())

data = {}
for item in modified:
    key, value = item.split('=')
    data[key.strip()] = value.strip()

# CONSTANTS
NAME=data["NAME"]
IF =data["IF"]
TP =data["TP"]
ICE =data["ICE"]
ZIP =data["ZIP"]
PHONE=data["PHONE"]
EMAIL=data["EMAIL"]
ADDRESS=data['ADDRESS']
RC=data["RC"]
WEBSITE=data["WEBSITE"]