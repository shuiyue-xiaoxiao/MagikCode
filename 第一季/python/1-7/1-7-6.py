Total = 0
Num = 0
Name = input("请输入菜名：")# your own code
while Name != "够了":
  Price = int(input("请输入价格："))# your own code
  Num = Num + 1# your own code
  Total = Total + Price# your own code
  Name = input("请输入下一道菜名：")# your own code
print("你总共点了" + str(Num) + "道菜。" + "总共花了" + str(Total) + "元。")
