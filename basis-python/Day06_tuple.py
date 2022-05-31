# -*- codeing = utf-8 -*-
# @Time :2022/5/31 20:25
# @Author :Jerry
# @Email  :jerry_09@aliyun.com
# @Version :1.0
# @Descriptioon :
# @File :  Day06_tuple.py
# 元组中元素不能被修改
a_tuples = (1, 2, 3, 4)
print(a_tuples)
print(a_tuples[0])

# 列表中元素是可以被修改的
a_list = [1, 2, 3, 4]
print(a_list[0])

a_list[3] = 5
print(a_list)

# 元组中如果是一个元素 那么他是整形 需要添加一个逗号
a_tuples = (5)
print(type(a_tuples))
a_tuples = (5,)
print(type(a_tuples))

# 切片
s = "hello world"
# 直接写下标访问元素内容
print(s[4])

# 包头不包尾 左闭右开
print(s[0:4])

# 从起始值开始一直到末尾
print(s[1:])

# 从下标为0的索引元素开始一直到第二个参数为止 左闭右开
print(s[:4])

# 从下标为0 字符长度-1 结束 每次增长2 左闭右开
print(s[0:len(s) - 1:2])
