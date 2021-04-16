#map(fun()which we used,when we applied)

lst=[10,20,30,21,40,25]
sq=list(map(lambda no:no**2,lst))
print(sq)
print(list(map(lambda no:no**3,lst)))
print(list(map(lambda no:no*.5,lst)))