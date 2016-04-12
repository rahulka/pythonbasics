a = 0

def my_function():
    global a
    a = 3
    print(a)

my_function()

print(a)

if a is 3 :
    print("some")