import requests

def test_fonction():
    pass

print(requests.__name__)
print(requests.__cake__)

print(test_fonction.__name__)

print(__name__)

x = 10

print(type(x))
print(type(requests))

for m in dir():
    print(m)

print(callable(x))
print(callable(test_fonction))

class A:
    pass

class B(A):
    pass

print(issubclass(A, B))
print(issubclass(B, A))

number = 100
text = 'hello'

print(isinstance(number, int))
print(isinstance(number, str))
print(isinstance(text, str))
print(isinstance(text,float))
print(isinstance(text, B))

import inspect

print(inspect.ismodule(requests))
print(inspect.ismodule(A))
print(inspect.ismodule(test_fonction))
print(inspect.getmodule(requests.get))
print(inspect.getmodule(list))

import sys

print(sys.version)
print(sys.executable)