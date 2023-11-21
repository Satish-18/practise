'''
DECORATOR
-->it peforms additional logic
-->or add specific logic to function
we can use @ to use decorator
'''
'''
#Double the number returns by another function
def decor(fun):
    def inner():
        result=fun()
        return result*2
    return inner
@decor
def num():
    return 5

print(num())
'''
#Decorator string
def decorfun(fun):
    def inner(n):
        result=fun(n)
        result+="How are u?"
        return result
    return inner
@decorfun
def hello(name):
    return 'helo'+name
print(hello("satish"))






