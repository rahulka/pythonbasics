#creating sets
a = {1, 2, 3, 4, 5, 6}
b = {5, 6, 7, 8, 9, 0}

print("a:" + str(a))
print("b:" + str(b))

#empty set
#c = {} is wrong, empty dict will be created
c = set()
print("c:" + str(c))

#operations
#union
print("Union:" + str(a | b))

#intersection
print("Intersection:" + str(a & b))

#subtraction, values in A which are not present in B
print("Subtraction:" + str(a - b))

#union minus intersection
print("union minus intersection:" + str(a ^ b))