# Python 基础语法入门

## 1. Python 简介

Python 是一种高级、解释型、通用的编程语言。它的设计哲学强调代码的可读性，并允许程序员用更少的代码行表达概念。

### Python 的特点
- **简洁易读**：语法接近自然语言
- **跨平台**：支持 Windows、macOS、Linux
- **丰富的库**：拥有庞大的标准库和第三方库
- **动态类型**：无需声明变量类型
- **面向对象**：支持面向对象编程

## 2. 变量和数据类型

### 2.1 变量定义
在 Python 中，变量不需要声明类型，直接赋值即可：

```python
# 变量定义
name = "张三"
age = 25
height = 1.75
is_student = True

# 打印变量
print(name)        # 输出：张三
print(age)         # 输出：25
print(height)      # 输出：1.75
print(is_student)  # 输出：True
```

### 2.2 基本数据类型

#### 数字类型
```python
# 整数 (int)
count = 100
negative = -50

# 浮点数 (float)
price = 19.99
pi = 3.14159

# 复数 (complex)
complex_num = 3 + 4j

print(type(count))      # <class 'int'>
print(type(price))      # <class 'float'>
print(type(complex_num)) # <class 'complex'>
```

#### 字符串类型
```python
# 字符串定义
name = "张三"
message = '你好，世界！'
multiline = """这是一个
多行字符串"""

# 字符串操作
print(name + " " + message)  # 字符串拼接
print(name * 3)              # 重复字符串
print(len(name))             # 字符串长度
print(name[0])               # 第一个字符
print(name[1:3])             # 切片操作
```

#### 布尔类型
```python
# 布尔值
is_true = True
is_false = False

# 布尔运算
result = is_true and is_false  # False
result = is_true or is_false   # True
result = not is_true           # False
```

#### 列表类型
```python
# 列表定义
fruits = ["苹果", "香蕉", "橙子"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# 列表操作
print(fruits[0])           # 访问第一个元素
fruits.append("葡萄")      # 添加元素
fruits.insert(1, "梨")     # 在指定位置插入
fruits.remove("香蕉")      # 删除元素
print(len(fruits))         # 列表长度
```

#### 字典类型
```python
# 字典定义
person = {
    "name": "张三",
    "age": 25,
    "city": "北京"
}

# 字典操作
print(person["name"])      # 访问值
person["email"] = "zhang@example.com"  # 添加键值对
person["age"] = 26         # 修改值
del person["city"]         # 删除键值对
print(person.keys())       # 获取所有键
print(person.values())     # 获取所有值
```

## 3. 控制结构

### 3.1 条件语句
```python
# if-elif-else 语句
score = 85

if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 70:
    grade = "中等"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"

print(f"成绩：{grade}")

# 三元运算符
status = "通过" if score >= 60 else "不通过"
print(status)
```

### 3.2 循环语句

#### for 循环
```python
# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"我喜欢{fruit}")

# 使用 range()
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)

# 遍历字典
person = {"name": "张三", "age": 25, "city": "北京"}
for key, value in person.items():
    print(f"{key}: {value}")
```

#### while 循环
```python
# 基本 while 循环
count = 0
while count < 5:
    print(f"计数：{count}")
    count += 1

# 带条件的 while 循环
number = 0
while number < 10:
    if number % 2 == 0:
        print(f"偶数：{number}")
    number += 1
```

#### 循环控制
```python
# break 语句
for i in range(10):
    if i == 5:
        break  # 跳出循环
    print(i)

# continue 语句
for i in range(10):
    if i % 2 == 0:
        continue  # 跳过本次循环
    print(i)

# else 子句
for i in range(5):
    print(i)
else:
    print("循环正常结束")
```

## 4. 函数

### 4.1 函数定义和调用
```python
# 基本函数定义
def greet(name):
    return f"你好，{name}！"

# 函数调用
message = greet("张三")
print(message)

# 带默认参数的函数
def greet_with_title(name, title="先生"):
    return f"你好，{title}{name}！"

print(greet_with_title("张三"))           # 使用默认参数
print(greet_with_title("李四", "女士"))    # 自定义参数
```

### 4.2 函数参数
```python
# 位置参数
def add(a, b):
    return a + b

print(add(3, 5))  # 8

# 关键字参数
def create_person(name, age, city="未知"):
    return {"name": name, "age": age, "city": city}

person1 = create_person("张三", 25, "北京")
person2 = create_person(age=30, name="李四", city="上海")

# 可变参数
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))  # 15

# 关键字可变参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="张三", age=25, city="北京")
```

### 4.3 匿名函数（Lambda）
```python
# Lambda 函数
square = lambda x: x ** 2
print(square(5))  # 25

# 在列表中使用
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# 过滤
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
```

## 5. 类和对象

### 5.1 基本类定义
```python
# 类定义
class Person:
    # 类属性
    species = "人类"
    
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # 实例方法
    def introduce(self):
        return f"我是{self.name}，今年{self.age}岁"
    
    def have_birthday(self):
        self.age += 1
        return f"{self.name}过生日了，现在{self.age}岁"

# 创建对象
person1 = Person("张三", 25)
person2 = Person("李四", 30)

# 调用方法
print(person1.introduce())
print(person1.have_birthday())
print(Person.species)  # 访问类属性
```

### 5.2 继承
```python
# 父类
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name}发出声音"

# 子类
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 调用父类构造函数
        self.breed = breed
    
    def speak(self):  # 重写父类方法
        return f"{self.name}汪汪叫"
    
    def fetch(self):
        return f"{self.name}去捡球"

# 使用继承
dog = Dog("旺财", "金毛")
print(dog.speak())    # 旺财汪汪叫
print(dog.fetch())    # 旺财去捡球
```

## 6. 异常处理

### 6.1 基本异常处理
```python
# try-except 语句
try:
    number = int(input("请输入一个数字："))
    result = 10 / number
    print(f"结果：{result}")
except ValueError:
    print("输入的不是有效数字")
except ZeroDivisionError:
    print("不能除以零")
except Exception as e:
    print(f"发生错误：{e}")
```

### 6.2 完整的异常处理
```python
# try-except-else-finally
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("错误：除数不能为零")
        return None
    except TypeError:
        print("错误：参数类型不正确")
        return None
    else:
        print("计算成功")
        return result
    finally:
        print("计算完成")

# 测试
print(divide_numbers(10, 2))   # 正常情况
print(divide_numbers(10, 0))   # 除零错误
print(divide_numbers(10, "a")) # 类型错误
```

## 7. 文件操作

### 7.1 文件读写
```python
# 写入文件
with open("example.txt", "w", encoding="utf-8") as file:
    file.write("这是第一行\n")
    file.write("这是第二行\n")
    file.write("这是第三行\n")

# 读取文件
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# 按行读取
with open("example.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() 去除换行符

# 逐行读取
with open("example.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

### 7.2 文件操作模式
```python
# 不同文件模式
# "r" - 只读模式（默认）
# "w" - 写入模式（覆盖）
# "a" - 追加模式
# "x" - 创建模式（文件不存在时创建）
# "b" - 二进制模式
# "t" - 文本模式（默认）

# 追加内容
with open("example.txt", "a", encoding="utf-8") as file:
    file.write("这是追加的内容\n")

# 二进制文件操作
with open("binary_file.bin", "wb") as file:
    data = b"Hello, World!"
    file.write(data)

with open("binary_file.bin", "rb") as file:
    data = file.read()
    print(data)
```

## 8. 模块和包

### 8.1 模块导入
```python
# 导入整个模块
import math
print(math.pi)
print(math.sqrt(16))

# 导入特定函数
from math import pi, sqrt
print(pi)
print(sqrt(16))

# 导入并重命名
import math as m
print(m.pi)

# 导入所有（不推荐）
from math import *
print(pi)
```

### 8.2 自定义模块
```python
# 创建 my_module.py 文件
# my_module.py 内容：
"""
这是一个自定义模块
"""

def greet(name):
    return f"你好，{name}！"

def add(a, b):
    return a + b

PI = 3.14159

# 在另一个文件中使用
# main.py 内容：
import my_module

print(my_module.greet("张三"))
print(my_module.add(3, 5))
print(my_module.PI)
```

## 9. 列表推导式和生成器

### 9.1 列表推导式
```python
# 基本列表推导式
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 带条件的列表推导式
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# 嵌套列表推导式
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### 9.2 生成器
```python
# 生成器函数
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# 使用生成器
for num in fibonacci(10):
    print(num)

# 生成器表达式
squares_gen = (x**2 for x in range(10))
print(list(squares_gen))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## 10. 总结

本章介绍了 Python 的基础语法，包括：

1. **变量和数据类型**：数字、字符串、布尔、列表、字典
2. **控制结构**：条件语句、循环语句
3. **函数**：定义、调用、参数、Lambda
4. **类和对象**：基本类、继承
5. **异常处理**：try-except 语句
6. **文件操作**：读写文件
7. **模块和包**：导入和使用
8. **高级特性**：列表推导式、生成器

这些是 Python 编程的基础，掌握这些内容后，您就可以开始编写简单的 Python 程序了。在下一章中，我们将学习如何搭建 Python 开发环境。
