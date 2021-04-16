def div_decor(func):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return func(n1,n2)
    return wrapper
@div_decor
def div(no1,no2):
    return no1/no2
res=div(.5,10)
print(res)