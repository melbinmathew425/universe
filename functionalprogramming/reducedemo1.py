#map and filter are in builtins.py
#but reduce in thefunctools
from functools import reduce
lst=[10,20,30,40,50]
total=reduce(lambda n1,n2:n1+n2,lst)
print(total)