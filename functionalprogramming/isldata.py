isldata=[
    {"team":"mumbai","mp":20,"drawn":4,"lost":4,"pts":48},
    {"team":"atk","mp":20,"won":12,"drawn":12,"lost":4,"pts":40},
    {"team":"NEu","mp":20,"won":8,"drawn":8,"lost":9,"pts":33},
    {"team":"fcgoa","mp":20,"won":7,"drawn":7,"lost":3,"pts":31},
    {"team":"hybad","mp":20,"won":6,"drawn":11,"lost":3,"pts":29}
]
print("no of team = ",len(isldata))
team_names=list(map(lambda tname:tname["team"],isldata))
print(team_names)
point=max(list(map(lambda pt:pt["pts"],isldata)))
print("max points =",point)
high_point=list(filter(lambda team:team["pts"]==point,isldata ))
print(high_point)
no1_team=list(map(lambda tname:tname["team"],high_point))
print(no1_team)
rangeteam=list(filter(lambda team: 30<team["pts"]<40,isldata))
print(rangeteam)
rangeteamname=list(map(lambda range:range["team"],rangeteam))
print(rangeteamname)