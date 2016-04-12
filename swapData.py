def swap(a, b):
    temp = a
    a = b
    b = temp


def changedata(inputData):
    inputData["newKey"] = "value"

if __name__ == "__main__":
    a = 3
    b = 4
    print("a:" + str(a) + " b:" + str(b))
    swap(a, b)
    print("a:" + str(a) + " b:" + str(b))

    a = {"k1": "v1", "k2": "v2"}
    b = {"k3": "v3", "k4": "v4"}
    print("a:" + str(a) + " b:" + str(b))
    swap(a, b)
    print("a:" + str(a) + " b:" + str(b))

    changedata(a)
    print("a:" + str(a) + " b:" + str(b))
