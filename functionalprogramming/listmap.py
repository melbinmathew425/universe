lst=[4,2,1,6,7,8]
#3,1,0,7,8,9 if no less than 5, sub 1. if no higher than 5, add 1.
result=list(map(lambda num:num+1 if num>5 else num-1,lst))
print(result)

