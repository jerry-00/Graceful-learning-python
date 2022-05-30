# -*- codeing = utf-8 -*-
# @Time :2022/5/30 14:05
# @Author :Jerry
# @Email  :jerry_09@aliyun.com
# @Version :1.0
# @Descriptioon :
# @File :  Day04_string.py

# 不能使用除了大小写字母数字_之外的数据命名 开头不允许使用数字 列如1_a
# 变量命名使用小驼峰 userName
letter = 'P'  # A string could be a single character or a bunch of texts
print(letter)  # P
print(len(letter))  # 1
print('------------------')

greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)  # Hello, World!
print(len(greeting))  # 13
print('------------------')

sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)
print('------------------')

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
print('------------------')

multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
print('------------------')

# String Concatenation
first_name = 'Asabeneh'
last_name = 'Yetayeh'
# 空格也算字符?
space = ' '
full_name = first_name + space + last_name
print(full_name)  # Asabeneh Yetayeh
# Checking length of a string using len() builtin function
print(len(first_name))  # 8
print(len(last_name))  # 7
print(len(first_name) > len(last_name))  # True
print(len(full_name))  # 15

#### Unpacking characters
language = 'Python'
# 将序列字符包裹在变量里
a, b, c, d, e, f = language
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n
print('python ----------------------')

# 通过索引访问变量中的某字符
language = 'Python'
first_letter = language[0]
# P
print(first_letter)
second_letter = language[1]
# Y
print(second_letter)
print('----------------------')
# 倒数第二个字符 n
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)
print('----------------------')

# 如果想从右端开始可以是负索引 与Java不同 python可以允许索引为负值.
language = 'Python'
# 结果为n
last_letter = language[-1]
print(last_letter)  # n
print('---------索引-1-------------')
second_last = language[-2]
print(second_last)  # o
print('---------索引-2-------------')

# 切割字符

language = 'Python'
# 索引从0开始最大为3但是不包含3 包左不包右
first_three = language[0:3]
print('包左不包右', first_three)
last_three = language[3:6]
print('包左不包右', last_three)

# 负值索引调用 0可以省略? -3 - 0
last_three = language[-3:]
print('包左不包右负值写法', last_three)
last_three = language[3:]
print('包左不包右', last_three)

# 拆分字符串时跳过字符
language = 'Python'
pto = language[0:6:2]
print('拆分字符串时跳过字符', pto)

# 转义序列
# \n 换行符
print('I hope every one enjoying the python challenge.\nDo you ?')
# \t 制表符
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
# 输出符号反斜杠 \
print('This is a back slash  symbol (\\)')
print('In every programming language it starts with \"Hello, World!\"')
# 输出转义符号内的特殊符号
print('测试1 \"Hello, World!\"')

# 字符串方法
# capitalize(): 将字符串的第一个字符转换为大写

challenge = 'thirty days of python'
print(challenge.capitalize())  # 'Thirty days of python'
abcdef = 'acb'
print(abcdef.capitalize())

# count() 返回字符串在 substring start=..,end=.. 中结束
challenge = 'thirty days of python'
# 统计字符串出现的次数 # 3
print('总长度为: ', len(challenge))
print(challenge.count('y'))
# 空格也算字符  # 1
print(challenge.count('y', 7, 14))
# 2`
print(challenge.count('th'))

# endswith(): 检查字符串是否以指定的结尾
challenge = 'thirty days of python'
print(challenge.endswith('on'))  # True
print(challenge.endswith('tion'))  # False

# expandtabs(): 将制表符替换为空格，默认制表符大小为8。它接受标签大小参数

challenge = 'thirty\tdays\tof\tpython'
# 'thirty  days    of      python'
print(challenge.expandtabs())
# 'thirty    days      of        python'
print(challenge.expandtabs(10))

# find(): 返回字符串第一次出现的索引

challenge = 'thirty days of python'
# 5
print(challenge.find('y'))
# 0
print(challenge.find('th'))
print('---格式化输出---')

# format()	输出好看的格式? 感觉没多大屁用 打印用的不会太多
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence)  # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi  # radius ## 2
# 需要时字符串格式 才能format
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result)

# index(): 返回子字符串的索引 返回命中字符串的索引
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th'))  # 0

print(challenge.startswith('t'))
print(challenge.endswith('n'))
print('=========替换=========')
print(challenge.replace('d', 's'))
challenge = 'thirty#days#of#python'
print('=========切割=========')
print(challenge.split("#"))
print('=========大小写=========')
print(challenge.upper() + challenge.lower())

# isalnum(): 检查字母数字类型
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())

challenge = '30DaysPython'
print(challenge.isalnum())

# 空格不是
challenge = 'thirty days of python'
print(challenge.isalnum())

challenge = 'thirty days of python 2019'
print(challenge.isalnum())

# isalpha(): 检查所有字符都是字母

challenge = 'thirty days of python'
print(challenge.isalpha())
num = '123'
# false
print(num.isalpha())

print("是否包含十进制数")
# isdecimal(): 是否包含十进制数
str = u"23443434"
print(str.isdecimal())

# isdigit(): 检查数字字符
challenge = 'Thirty'
print(challenge.isdigit())  # False
challenge = '30'
print(challenge.isdigit())
print('---isdigit---')

# isdecimal():是否包含十进制数
num = '10'
print(num.isdecimal())
num = '10.5'
print(num.isdecimal())
print('---包含十进制数---')

# isidentifier():检查是否是有效变量名
challenge = '30DaysOfPython'
print(challenge.isidentifier())  # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())  # True
challenge = 'thirtyDaysOfPython'
print(challenge.isidentifier())  # True
print('---有效变量名---')

# islower():是否都小写
challenge = 'thirty days of python'
print(challenge.islower())  # True
challenge = 'Thirty days of python'
print(challenge.islower())  # False
print('---都小写---')

# isupper(): 都大写

challenge = 'thirty days of python'
print(challenge.isupper())  # False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper())  # True

# isnumeric():检查数字字符
num = '10'
print(num.isnumeric())
print('ten'.isnumeric())

# join(): 返回连接字符串
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
# 'HTML# CSS# JavaScript# React'
print(result)

print('---移除首尾字符---')
# strip(): 移除收尾字符
challenge = 'www.baidu.com'
print(challenge.strip('wcom.'))
# 含w的都被移除 .baidu.com
print(challenge.strip('w'))
# baidu.com
print(challenge.strip('w.'))
print('............')

# replace(): 替换字符串
challenge = 'thirty days of python'
# thirty days of coding
print(challenge.replace('python', 'coding'))

# split():从左拆分字符串 空格可以算清空 其他符号不行
challenge = 'thirty days of python'
# ['thirty', 'days', 'of', 'python']
print(challenge.split())

# title(): 返回一个大小写区分的字符串
challenge = 'thirty days of python'
# Thirty Days Of Python
print('标题大小写: ', challenge.title())

# swapcase(): 检查字符串是否是从指定字符串开始
challenge = 'thirty days of python'
print(challenge.swapcase())  # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): 检查字符串是否是指定字符串开始
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))
challenge = '30 days of python'
# False
print(challenge.startswith('thirty'))

# 转换类型
a = '123'
print(type(a))
print(int(a))
b = int(a)
print(type(b))

# 浮点转换
a = 1.23
print(type(a))
b = int(a)
print(type(b))
# 取整 不保留小数
print(b)
# boolean -> int 1 / 0
a = True
b = int(a)
print(type(b))
print(b)

# 含有非法字符 . 无法转换 爬虫大部分都是获取字符串类型 今后要转换为浮点
a = '1.23'
# b = int(a)
c = float(a)
print(c)
print(type(c))
print('去除空格')
bb = ' a '
print(len(bb.strip()))
