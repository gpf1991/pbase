# 练习:
#   1. 写一个程序, 模拟斗地主发牌,牌共54张
#     种类有: 黑桃('\u2660'), 梅花('\u2663'),
#            红桃('\u2665'), 方块('\u2666)
#     数字有: A2-10JQK
#     大王和小王
#     输入回车, 打印第1个人的17张牌
#     输入回车, 打印第2个人的17张牌
#     输入回车, 打印第3个人的17张牌
#     输入回车, 打印3张底牌


poke = ['大王', '小王']

kinds = ['\u2660','\u2663', '\u2665', '\u2666']  # 种类
numbers = ['A']
numbers += [str(x) for x in range(2, 11)]
numbers += list("JQK")

for x in kinds:
    for y in numbers:
        poke.append(x + y)

assert len(poke) == 54, '出错!'

# 洗牌
poke2 = poke.copy()  # 复制一副新牌(保留旧牌)
import random
random.shuffle(poke2)

player1 = poke2[:17]
player2 = poke2[17:34]
player3 = poke2[34:51]
base = poke2[51:]

# 输入回车, 打印第1个人的17张牌
input()
print("第1个人的17张牌是", player1)
# 输入回车, 打印第2个人的17张牌
input()
print("第2个人的17张牌是", player2)
# 输入回车, 打印第3个人的17张牌
input()
print("第3个人的17张牌是", player3)
# 输入回车, 打印3张底牌
input()
print("三张底牌是:", base)

