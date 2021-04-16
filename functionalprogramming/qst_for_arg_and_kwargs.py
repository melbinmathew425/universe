employe={1000:{"name":"anu","desig":"hr","ex":3},
         1001:{"name":"manu","desig":"developer","ex":6},
         1002:{"name":"binu","desig":"r&d","ex":4}}

eid=int(input("enter a eid"))
if (eid in employe):
    print(employe[eid]["name"])
else:
    print("id not exist")



