# -*- codeing = utf-8 -*-
# @Time :2022/5/30 14:04
# @Author :Jerry
# @Email  :jerry_09@aliyun.com
# @Version :1.0
# @Descriptioon :
# @File :  Day03_Arithmetic.py
print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
# 给浮点数
print('Division: ', 4 / 2)
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
# 不带浮点或者余数 取整
print('Division without the remainder: ', 7 // 2)
# 余数
print('Modulus: ', 3 % 2)
print('Division without the remainder: ', 7 // 3)
print('指数: ', 3 ** 2)

# 浮点类型数
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# 复数 不怎么用
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ', (1 + 1j) * (1 - 1j))
print('----------------------------')

num_one = 3
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('浮点: ', div)
print('求余: ', remainder)
print('----------------------------')

# 计算圆的面积
radius = 10
area_of_circle = 3.14 * radius ** 2
print("圆面积为: ", area_of_circle)
print('----------------------------')

# 计算物体的重量
mass = 75
gravity = 9.135
weight = mass * gravity
print("重量为: ", weight, "N")
print('----------------------------')

print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 < 3)
print(2 <= 3)
print(3 == 2)
# True
print(3 != 2)
print('----------------------------')

print(len('mango') == len('avocado'))
print(len('mango') != len('avocado'))
# True 判断的是字符串长度
print(len('mango') < len('avocado'))
# false
print(len('milk') != len('meat'))
print(len('milk') == len('meat'))
print(len('tomato') == len('potato'))
# false
print(len('python') > len('dragon'))
print('----------------------------')

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
# 或 True
print('True or False:', True or False)
print('----------------------------')

print('1 is 1', 1 is 1)
print('1 is not 2', 1 is not 2)
# 包含字符串 区分大小写
print('A in Asabeneh', 'A' in 'Asabeneh')
# 区分大小写
print('B in Asabeneh', 'B' in 'Asabeneh')
print('coding' in 'coding for all')
print('a in an:', 'a' in 'an')
# 2^2
print('4 is 2 ** 2:', 4 is 2 ** 2)
print('----------------------------')

# True 类似java的&&
print(3 > 2 and 4 > 3)
# false
print(3 > 2 and 4 < 3)
# False
print(3 < 2 and 4 < 3)
# True java的||
print(3 > 2 or 4 > 3)
print(3 > 2 or 4 < 3)
print(3 < 2 or 4 < 3)
# 取反 not true False
print(not 3 > 2)
print(not True)
print(not False)
# 一般不会这样写吧...
print(not not True)
print(not not False)
