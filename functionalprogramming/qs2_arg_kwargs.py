employe={1000:{"name":"anu","desig":"hr","ex":3},
         1001:{"name":"manu","desig":"developer","ex":6},
         1002:{"name":"binu","desig":"r&d","ex":4}}

def print_emp(**data):#data={eid:1001}
    id=data["eid"]
    if id in employe:
        print(employe[id]["name"])
    else:
        print("id not exist")

print_emp(eid=1001)
print_emp(eid=1008)