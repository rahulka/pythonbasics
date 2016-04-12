class Complex:

    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    # takes the latest definition
    # there is no concept of overloading
    def __init__(self):
        self.i = 0
        self.r = 0

    def __repr__(self):
        print(str(self.r) + " +" + str(self.i) + " i")

    def __str__(self):
        return str(self.r) + " +" + str(self.i) + " i"


if __name__ == "__main__":
    complex1 = Complex()
    print("complex:" + str(complex1))


