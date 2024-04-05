import math

# 引导用户输入两个角的度数和夹边的长度
angle1 = float(input("请输入第一个角的度数："))
angle2 = float(input("请输入第二个角的度数："))
side = float(input("请输入夹边的长度："))

# 计算第三个角的度数
angle3 = 180 - angle1 - angle2

# 计算第三边的长度
side1 = side * math.sin(math.radians(angle1)) / math.sin(math.radians(angle3))
side2 = side * math.sin(math.radians(angle2)) / math.sin(math.radians(angle3))
# 输出结果
print("第二边的长度为：", side1)
print("第三边的长度为：", side2)
