a = {'max':{}, 'ann':{}, 'kate':{}}
print(a)
print(a['ann'])

for i in a:
    a[i]['him'] = []

for i in a:
    a[i]['mat'] = []


print(a)

a['max']['him'].append(4)
print(a)
a['max']['him'].append(5)
print(a)
print()

print(a.keys())
print(type(a.keys()))
print()

print(a.values())
print(type(a.values()))

b = a.values()
print(b)