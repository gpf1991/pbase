#   2. 一个小球从100米高空落下,每次落地后反弹高度为原高度的一半
#     再落下,
#     1) 写程序算出皮球在第10次落地后反弹多高
#     2) 打印出第10次反弹后小球经历的总路程


def get_last_height(meter, times):
    '''此函数计算小球从meter高度下落反弹 times次后
    最终的高度,并返回'''
    for _ in range(times):
        meter /= 2
    return meter

print("小球从100米高下落十次后的反弹高度是:", 
      get_last_height(100, 10))

def get_distance(meter, times):
    '''此函数计算小球从meter高米下落times次反弹高度,
    并返回 
    '''
    s = 0
    for _ in range(times):
        # 累加下落高度
        s += meter
        meter /= 2  # 算出反弹高度
        s += meter  # 累加反弹高度
    return s

print("小球从100米下落反弹十次后经历的路程是:", 
      get_distance(100, 10))

