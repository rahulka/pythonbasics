__author__ = 'redpanda'

# import  odbchelper

# params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
# print odbchelper.buildConnectionString(params)
# print odbchelper.buildConnectionString.__doc__

no_chickens = "No chickens here..."
def append_chickens(text):
    text = text + " Rawwwk!"
    return text

print(append_chickens(no_chickens))