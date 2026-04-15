class Numbers:
    def __init__(self, a=None, b=None, c=None):
        if a is None and b is None and c is None:
            self.n1 = 1
            self.n2 = 2
            self.n3 = 3

        elif b is None and c is None:
            self.n1 = a
            self.n2 = a 
            self.n3 = a

        else:
            self.n1 = a
            self.n2 = b
            self.n3 = c

    def display (self):
        print(f"n1 = {self.n1}\tn2 = {self.n2}\tn3 = {self.n3}")

obj1 = Numbers()
obj2 = Numbers(100)
obj3 = Numbers(12, 32, 23)

obj1.display()
obj2.display()
obj3.display()
