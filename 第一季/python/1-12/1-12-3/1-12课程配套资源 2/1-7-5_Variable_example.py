# 1-7-5_Variable example
# 思考：如何从1加到100

# 命名2个变量
a = 1
Sum = 0

# 使用 While 循环
while a <= 100:
    Sum = Sum + a # 现在的Sum = 上一个Sum + 上一个a
    a += 1 # 现在的a = 上一个a + 1 (当 101 = 100 + 1 时，推出循环)

# 打印结果
print(Sum)

