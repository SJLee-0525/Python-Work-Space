a = {'a':1, 'b':2}

# print(a['c']) # KeyError: 'c'

print(a.get('c')) # None

print(a.get('c', 3)) # 3

print(a)

print(a.setdefault('c', 3)) # None
# {'a': 1, 'b': 2, 'c': None}

# print(a.setdefault('c', 3))

print(a)