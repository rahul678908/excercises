x = lambda a: a+10
print(x(5))

#multiplying argument a with argument b

x = lambda a,b: a*b
print(x(5,6))

x = lambda a,b,c: a+b+c
print(x(3,4,5))

#in a function

def myfunc(n):
    return lambda a:a*n
mydoubler = myfunc(2)
print(mydoubler(11))

def myfunc(n):
    return lambda a:a*n
mytripler = myfunc(3)
print(mydoubler(11))
