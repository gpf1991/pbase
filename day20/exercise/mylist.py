# 练习:
#   1. 实现两个自定义列表相加
#     class MyList:
#         def __init__(self, iterable=()):
#             ...
#         ...

#     L1 = MyList([1, 2, 3])
#     L2 = MyList(range(4, 7))
#     L3 = L1 + L2
#     print(L3)  # MyList([1, 2, 3, 4, 5, 6])
#     L4 = L2 + L1
#     print(L4)  # MyList([4, 5, 6, 1, 2, 3])
#     L5 = L1 * 2
#     print(L5)  # MyList([1, 2, 3, 1, 2, 3])




class MyList:
    def __init__(self, iterable=()):
        '''此处用给定的可迭代对象iterable创建一个新的列表,
        绑定此对象的data 实例变量中'''
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    def __mul__(self, rhs):
        return MyList(self.data * rhs)

L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 7))
L3 = L1 + L2  # L3 = L1.__add__(L2)
print(L3)  # MyList([1, 2, 3, 4, 5, 6])
L4 = L2 + L1  # L4 = L2.__add__(L1)
print(L4)  # MyList([4, 5, 6, 1, 2, 3])

L5 = L1 * 2
print(L5)  # MyList([1, 2, 3, 1, 2, 3])

# L6 = 2 * L1  # L6 = 2.__mul__(L1)
# print(L6)  # ?????

