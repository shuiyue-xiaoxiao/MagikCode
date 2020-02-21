'''

1-8-3 The value in the list
列表是有序的，列表中的每一个数据项(元素)都带有自带的位置信息，称之为“索引”
列表的“索引”从零开始

'''

# 声明一个list变量，变量名为list1，并给变量list1赋值
list1 = [ 1, 2, 3, 4, 5]
# 声明一个list变量，变量名为list2，并给变量list2赋值
list2 = [ "a", "b", "c", "d", "e"]
# 声明一个list变量，变量名为list3，并给变量list3赋值
list3 = [ "Thanksgiving", "Helloween", "Christmas", ]
# 声明一个list变量，变量名为list4，并给变量list4赋值
list4 = [ True,False]
# 声明一个list变量，变量名为list5，并给变量list5赋值
list5 = [ 1, "a", "Thanksgiving", "False", "a", "r", 4, 5]


# 访问 list1 中第3个数据项(元素)
print(list1)
print("list1[2]:", list1[2])
print()

# 访问 list2 中第1~4的数据项(元素)
print(list2)
print("list2[1:4]:", list2[1:4])
print()

# 访问 list3 中第倒数第一个数据项(元素)
print(list3)
print("list3[-1]:", list3[-1])
print()

# 访问 list4 中第倒数第二个数据项(元素)
print(list4)
print("list4[-2]:", list4[-2])
print()

# 访问 list5 中第1～6的数据项(元素)
print(list5)
print("list5[1:6]:", list5[1:6])









