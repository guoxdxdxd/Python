# 任务：创建一个简单的学生管理系统
# 功能：添加学生、删除学生、查找学生、显示所有学生

class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major


class StudentManager:
    # 你的代码：
    def __init__(self, students=[]):
        self.students = students

    def add_student(self, name, age, major):
        student = Student(name, age, major)
        self.students.append(student)

    def show_all_students(self):
        for student in self.students:
            print(f"姓名：{student.name}, 年龄：{student.age}, 专业：{student.major}")

    def find_student(self, name):
        for student in self.students:
            if student.name == name:
                return student

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
    pass


# 测试
manager = StudentManager()

# 添加学生
manager.add_student("张三", 20, "计算机科学")
manager.add_student("李四", 19, "数学")
manager.add_student("王五", 21, "物理")

# 显示所有学生
print("所有学生：")
manager.show_all_students()

# 查找学生
student = manager.find_student("张三")
if student:
    print(f"\n找到学生：{student.name} 年龄 {student.age}")

# 删除学生
manager.remove_student("李四")
print("\n删除李四后的学生列表：")
manager.show_all_students()
