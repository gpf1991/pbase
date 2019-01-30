
# 练习:
#   自己实现一个myenumerate函数,功能与enumerate功能完全一致
#   如:
#     def myenumerate(iterable, start=0):
#         ... # 此处自己实现
    
#     for t in myenumerate(names, 101):
#         print(t)  # (101, '中国移动'), (102, ....)



# def myenumerate(iterable, start=0):
#     return enumerate(iterable, start)

# # 方法1
# def myenumerate(iterable, start=0):
#     it = iter(iterable)  # 先拿到iterable的迭代器
#     while True:
#         try:
#             x = next(it)
#             yield (start, x)
#             start += 1
#         except StopIteration:
#             return

# 方法2
def myenumerate(iterable, start=0):
    for x in iterable:
        yield (start, x)
        start += 1

names = ['中国移动', '中国电信', '中国联通']
for t in myenumerate(names, 101):
    print(t)  # (101, '中国移动'), (102, ....)

        
        
