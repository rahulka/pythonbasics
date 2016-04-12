# list is mutable
# list is ordered
# index based lookup

li = ["a", "b", "el", "sda"]
print("li:" + str(li))

# can use list() on other data structures

# add data
# insert : inserts a single element into a list. The numeric argument is the index of the first element that gets
#            bumped out of position
li.insert(3, "mass")
print("li after li.insert(3,\"mass\"):" + str(li))

# append : append the element to the list
li.append("matter")
print("li after li.append(\"matter\"):" + str(li))

# extend : add multiple elements in the list
li.extend(["something", "else"])
print("li after li.extend([\"something\", \"else\"]):" + str(li))

# append vs extend : extend adds each of the elements in the argument(can be list only) list to the original list
# append just adds the argument(can be of any type)to the list
li.extend(["more"])
print("li after li.extend([\"more\"]):" + str(li))

# nesting of lists
li.append(["doc", "element"])
print("li after li.append([\"doc\", \"element\"]):" + str(li))

# retrieve data
print("li[0]:" + li[0])

# negative index
# consider them as li[-index] = li[len - index]
print("li[-1]:" + str(li[-1]))
print("li[-2]:" + li[-2])

# slicing
# li = [0, 1, 2, 3, 4]
# li[1:3] => [1, 2] so li[1], li[2]
# li[idx:n] =>  li[idx], li[idx + 1], ... li[n-1]
print("li[1:3]" + str(li[1:3]))

# shorthand
# li[:] copy of list
print("li[:]" + str(li[:]))

# li[:3] start from 0
print("li[:3]" + str(li[:3]))

# li[2:] till end of the list
print("li[2:]" + str(li[2:]))

# searching lists
# ValueError when element is not found
print("li.index('matter'):" + str(li.index('matter')))

print("\"matter\" in li:" + str("matter" in li))

# remove element from list
li.remove("sda")
print("li after li.remove(\"sda\"):" + str(li))

# operators
li = li + ["temp"]
print("li = li + [\"temp\"]:" + str(li))

# multiply the elements times 3 and assign to the new list
li2 = [1, 2] * 3
print("li2 = [1, 2] * 3:" + str(li2))

# pop
print("li.pop():" + li.pop())
print("li after pop:" + str(li))

# count element occurrences
print("li.count('el'):" + str(li.count('el')))

# delete operations
del li[2]
print("After del li[2]:" + str(li))

del li[3:5]
print("After del li[3:5]:" + str(li))

# list comprehensions
squares = [x**2 for x in range(10)]
print("squares:" + str(squares))

"""
A list comprehension consists of brackets containing an expression followed by a for clause,
then zero or more for or if clauses.
The result will be a new list resulting from evaluating the expression in the context of the for
and if clauses which follow it.
"""
print("List comprehensions:")
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])