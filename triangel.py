class Triangle:
    a = 0
    b = 0
    c = 0

    def __init__(self):
        self.a = int(input("A: "))
        self.b = int(input("B: "))
        self.c = int(input("C: "))

    def perimeter(self):
        per = self.a + self.b + self.c
        return per

p = Triangle()
print(p.perimeter())



