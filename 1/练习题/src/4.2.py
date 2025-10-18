# 任务：创建动物类及其子类
# 动物类：名称、年龄、发出声音
# 狗类：继承动物类，重写发出声音方法，添加品种属性
# 猫类：继承动物类，重写发出声音方法，添加颜色属性

class Animal:
    # 你的代码：
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"我是一个动物，我的名字是{self.name}，年龄是{self.age}岁。"
    def make_sound(self):
        return "动物叫"
    pass

class Dog(Animal):
    # 你的代码：
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    def make_sound(self):
        return "小狗叫"
    pass

class Cat(Animal):
    # 你的代码：
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        return "小喵叫"
    pass

# 测试
dog = Dog("旺财", 3, "金毛")
cat = Cat("咪咪", 2, "橘色")

print(dog.introduce())
print(dog.make_sound())
print(f"品种：{dog.breed}")

print(cat.introduce())
print(cat.make_sound())
print(f"颜色：{cat.color}")