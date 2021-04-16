#pick words starting with a
lst=["anu","vinu","arun","bibin","ammu","gopan"]
aname=list(filter(lambda name:name[0]=='a',lst))
print(aname)