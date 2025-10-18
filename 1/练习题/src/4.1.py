# 任务：创建一个学生类
# 属性：姓名、年龄、成绩
# 方法：介绍自己、计算平均分、判断是否及格

class Student:
    # 你的代码：
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)
    def is_passing(self):
        return self.calculate_average() >= 60
    def introduce(self):
        return f"我是{self.name}，今年{self.age}岁，我的成绩是{self.scores}"

# 测试
student1 = Student("张三", 20, [85, 90, 78])
student2 = Student("李四", 19, [92, 88, 95])

print(student1.introduce())
print(f"平均分：{student1.calculate_average()}")
print(f"是否及格：{student1.is_passing()}")

print(student2.introduce())
print(f"平均分：{student2.calculate_average()}")
print(f"是否及格：{student2.is_passing()}")