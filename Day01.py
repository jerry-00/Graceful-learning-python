# -*- codeing = utf-8 -*-
# @Time :2022/5/30 14:01
# @Author :Jerry
# @Email  :jerry_09@aliyun.com
# @Version :1.0
# @Descriptioon :
# @File :  Day01.py
# 单行注释
print('things')

# 我是注释 ctrl+?
''' 
多行注释 单引号
'''

print('变量的定义')
a = 'aaaaaa'
b = 'bbbb'
print(a + b)

'''
python的数据类型
numbers int long(python3废除) float(浮点) complex(复数)不咋用
布尔 True False
string 字符串 'aaa'
list 列表 
tuple 元组 与列表类似 一个数据代表一个元素集合
dictionary 字典
'''

# 数值
# 自动数据类型匹配
money = 5000
# float
money1 = 1.2
# 布尔
sex = True

# 单引号字符串或者双引号
s = '我我我'
d = "我我我我"
# 单双引号嵌套 傻缺写法 不考虑
f = '"我我我"'

'''
列表 元组 字典
'''
# 数组的感觉
name_list = ['ww', "www"]
# 动态列表?
name_file = [10]
print(name_list)
print(type(name_list))

# 元组
age_tuple = (10, "11", 100)
print(age_tuple)
print(type(age_tuple))

# 字典 类似map kv格式
person = {'name': 12, 'age': 100}
print(person)
print(type(person))

# 变量是没有类型的有类型的是数据 空 非null
person = {}
print(person)

# 判断数据类型 type of
a = 1
print(type(a))

# 运算
print(2 + 3)
print(3 / 2)
# 9 3^2
print(3 ** 2)
# 1
print(3 % 2)
# 1
print(3 // 2)
# Complex
print(type(1 + 3j))
# set
print(type({9.8, 3.14, 2.7}))
# Tuple 元组类型
print(type((9.8, 3.14, 2.7)))
