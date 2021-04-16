employe={1000:{"name":"anu","desig":"hr","ex":3},
         1001:{"name":"manu","desig":"developer","ex":6},
         1002:{"name":"binu","desig":"r&d","ex":4}}
def print_data(**data):
    id=data["eid"]
    prop=data["prop"]
    if id in employe:
        print (employe[id]["name"])
        print(employe[prop]["desig"])
    else:
        print("id not exist")

print_data(eid=1000,prop="desig")

