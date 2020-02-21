# 1-8-2
# 数据结构(列表)
# (1):
list2 = [123, 76, 676, 54, 35, 654, 56, 65, 6765, 43, 5456, 45, 78, 734, 56]
print(list2[1])
print(list2[2])
print(list2[0])
print(list2[3])
print(list2[5])
print(list2[6])
print(list2[8])
print(list2[7])
print(list2[9])
print(list2[4])
print(list2[12])
print(list2[14])
print(list2[11])
print(list2[13])
print(list2[10])

print()

# (2):
list2 = []

import random
Num = 15
for i in range(Num):
    list2.append(random.randint(1, 10000000000))

for i in range(Num):
    print(list2[i])
