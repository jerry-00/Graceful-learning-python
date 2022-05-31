# -*- codeing = utf-8 -*-
# @Time :2022/5/31 20:39
# @Author :Jerry
# @Email  :jerry_09@aliyun.com
# @Version :1.0
# @Descriptioon :
# @File :  Day07_dictionary.py
# 定义一个字典
person = {'name': '吴亦凡', 'age': 28}

# 访问person的name
print(person['name'])
print(person['age'])

# 获取空key时会返回None 但不报错
print(person.get('name'))
