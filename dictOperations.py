# dict is mutable
# unordered set of key: value pairs
# dictionary keys are case sensitive

# create dicts
d = {
    'server': 'localhost',
    'port': '8080',
    'contextRoot': 'app',
    'username': 'admin',
    'password': 'admin'
}

print ("d:" + str(d))

# empty dict
d1 = {}
print('d1:' + str(d1))

# dict constructor
d2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print('d2:' + str(d2))

d3 = dict(sape=4139, guido=4127, jack=4098)
print('d3:' + str(d3))

# dict comprehension
d4 = {x:x**2 for x in [1, 2, 3, 4]}
print('d4:' + str(d4))

# retrieval
print("d['server']:" + d['server'])

# dictionary keys are case sensitive
# throws KeyError
# print(d['Port'])

# checking if key is present in dictionary
if 'server' in d:
    print('server key is present in dictionary d')

# dict functions
print('d.keys():' + str(d.keys()))

print ("d.has_key('server'):" + str(d.has_key('server')))

# get value by key with optional also
print ("d.get('server', 'domain'):" + str(d.get('server', 'domain')))
print ("d.get('server1', 'domain'):" + str(d.get('server1', 'domain')))

# copy
d5 = d.copy()
print('d5:' + str(d5))

# items
print("d.items:" + str(d.items()))
print("d.items()[0]:" + str(d.items()[0]))
print("type(d.items()[0]:" + str(type(d.items()[0])))

# pop returns the value of the given key and removes element from dict
print("d before pop:" + str(d))
popped = d.pop('server')
print("popped:" + popped)
print("d after pop operation:" + str(d))

# popItem returns the tuple from top of the collection and removes it from dict
print("d before popitem:" + str(d))
poppedItem = d.popitem()
print("poppedItem:" + str(poppedItem))
print("d after popitem operation:" + str(d))

# setDefault : AFAIK it adds the element in the dict and will return value if looked up by key
print("d before setdefault:" + str(d))
d.setdefault('protocol', 'http')
print("d after setdefault:" + str(d))
print("str(d['protocol']):" + str(d['protocol']))

# update : adds elements in the doc, if same overrides the existing
print("d4 update:" + str(d4))
d4.update({1:1, 2:4, 3:6, 5:25})
print("d4 after update:" + str(d4))

# delete an element from the list
del d4[1]
print("d4 after del d4[1]:" + str(d4))

# get items and values
print d.viewitems()
print(d.viewvalues())

# using dict internal function
print d.__str__()

# clear dict, remove all elements
d.clear()
print("after clearing d:" + str(d))


# nesting of dictionaries
