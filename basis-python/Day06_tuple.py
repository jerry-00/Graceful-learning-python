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
