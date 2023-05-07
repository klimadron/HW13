import requests
from datetime import datetime

current_dateTime = datetime.now()
########################1##########################
x = input("Введи кол-во параграфов: ")
payload = {'paras': x, 'format': 'json'}
r = requests.get("https://baconipsum.com/api?type=meat-and-filler", params=payload).text
r = r.strip('][}{')
data = ['"{}"'.format(r) for r in r.split('"') if r not in ('', ',')]
###########################2#########################
list.reverse(data)
count = 0
##############################3######################################
for p in data:
    if "Pancetta" in p:
        count += 1
##############################4###############################
with open('hw13.txt', 'w') as writer:
    writer.write("Author: Andrew Klimakhin\n")
    writer.write(f"Starting time: {current_dateTime}\n")
    writer.write(f"Pancetta word counter: {count}\n")
    writer.write("\n".join(data))
    writer.close()
#
# for p in data:
#
#
# writer.write(f"{p}\n")
