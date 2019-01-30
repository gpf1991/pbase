
# 此示例示意一元运算符的重载
class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __neg__(self):
        gen = (-x for x in self.data)
        return MyList(gen)

    def __pos__(self):
        gen = (abs(x) for x in self.data)
        return MyList(gen)

    def __invert__(self):
        return MyList(reversed(self.data))

L1 = MyList([1, -2, 3, -4, 5])

L2 = - L1  # L2 = L1.__neg__()
print("L2=", L2)  # MyList([-1, 2, -3, 4, -5])
L3 = + L1
print("L3=", L3)  #  MyList([1, 2, 3, 4, 5])
L4 = ~ L1
print("L4=", L4)  # MyList([5, -4, 3, -2, 1])

