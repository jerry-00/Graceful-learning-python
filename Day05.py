# -*- codeing = utf-8 -*-
# @Time :2022/5/30 14:05
# @Author :Jerry
# @Email  :jerry_09@aliyun.com
# @Version :1.0
# @Descriptioon :
# @File :  Day05.py

# 整形转字符串
a = 6
print(type(a))
b = str(a)
print(b)
print(type(b))

t = True
print("布尔类型: ", t)
f = str(t)
print("转换为字符串类型:", f)
print(type(f))

# 如果对非0 的数进行布尔转换 都为True 包含正数和负数 除了浮点 0.0 整数0 字符串有内容 转bool为True
a = 2
print(type(a))
b = bool(a)
print("非0数转换bool: ", b)
print(type(b))

a = ' '
print(type(a))
b = bool(a)
print("非0数转换bool: ", b)
print(type(b))

# 列表类型
a = ["aaa", "bbbb"]
print(a)
print(type(a))
# 元组类型
a = ('aa', 'bbb', "ccc")
print(a)
print(type(a))
# python3与其他语言有所不同,对于数组的索引可以有负值,对其他数据类型转换为布尔型较为宽松,只要不是0,0.0,空值都为True
# 赋值运算符
d, e, f = 1, 2, 'aaa'
print(d, e, f)
# 复合赋值运算符 a = a+2
a = 1
a += 2
print(a)
a *= 3
print(a)
a **= 2
print(a)
# 格式化输出 scrapy框架 导出Excel文件 MySQL Redis
age = 18
name = '啊啊啊'
# %s 字符串 %d数值
print('我的名字%s,我的年龄%d' % (name, age))

# 输入
# password = input('输入文字......')
# print('密码是%s' % password)

# if 关键字语句结构
if age > 18:
    # 必须留tab
    print("两位数了...")
else:
    print("false")

# score = int(input('输入分数....'))

# if score >= 90:
#     print("优秀")
# elif score >= 80:
#     print("良好")
# elif score >= 70:
#     print("中")
# else:
#     print("差")

# for循环
s = 'wofnsongadfa'
# i 是字符串中一个又一个的字符串的变量 s是要遍历的数据
# for i in s:
#     print(i)

# 左闭右开 0 1 2 3 4 range结果是一个可以遍历的对象
for i in range(5):
    print(i)
# 起始值和结束值
for i in range(1, 5):
    print(i)
# 起始值 结束值 步长 1 4 7 10
for i in range(1, 11, 3):
    print(i)

# 场景应用 会爬取一个列表返回 循环一个列表 这个range很合适用来遍历数组类型元素 下标值不需要 以往的length-1 更精简
a_list = ['a', 'b', 'c']
for i in range(len(a_list)):
    print(i)
# 列表的添加 append 尾部添加
print(a_list.append('wo'))
print(a_list)

# insert 通过下标插入
a_list.insert(1, 'c')
print(a_list)

# extend 将一个列表元素追加到列表后
b_list = ['1', '3']
a_list.extend(b_list)
print(a_list)

# 类表的修改 修改列表中的元素之 就是通过下标修改
a_list[0] = '9'
print(a_list)

# 列表查找 下标负数查找 倒数第一第二
print(a_list[-1])
print(a_list[-2])

fruits = ['banana', 'orange', 'mango', 'lemon']
# 打印所有
all_fruits = fruits[-4:]
# -3和-1 包头不包尾 it does not include the end index
orange_and_mango = fruits[-3:-1]
# -3后所有
orange_mango_lemon = fruits[-3:]
print(all_fruits, orange_and_mango, orange_mango_lemon)

# remove 值删除
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.remove('banana')
print(fruits)

# pop 删除最后一个元素
fruits.pop()
print(fruits)

# del 下标删除
del fruits[0]
print(fruits)

# clear 清空
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)

# copying a lits
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)

# join 就是尾部添加
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# count 统计出现次数
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))  # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))

# index 得出对应下标
fruits = ['banana', 'orange', 'mango', 'lemon']
print('orange 在list中位于第' + str(fruits.index('orange')))

# Reverse 反转
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits)

# sort 排序 字符串情况下字母表顺序排序
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
# 数字排序
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
