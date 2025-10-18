# 任务：创建一个文件操作程序
# 1. 写入学生信息到文件
# 2. 从文件读取学生信息
# 3. 追加新的学生信息

def write_students_to_file(students, filename):
    """
    将学生信息写入文件

    Args:
        students: 学生信息列表
        filename: 文件名
    """
    # 你的代码：
    file = open(filename, "w", encoding="utf-8");
    for student in students:
        file.write(f"{student['name']},{student['age']},{student['grade']}\n")
    pass


def read_students_from_file(filename):
    """
    从文件读取学生信息

    Args:
        filename: 文件名

    Returns:
        学生信息列表
    """
    # 你的代码：
    file = open(filename, "r", encoding="utf-8");
    students = []
    for line in file:
        name, age, grade = line.strip().split(",")
        students.append({"name": name, "age": age, "grade": grade})
    return students
    pass


def append_student_to_file(student, filename):
    """
    追加学生信息到文件

    Args:
        student: 学生信息
        filename: 文件名
    """
    # 你的代码：
    file = open(filename, "a", encoding="utf-8");
    file.write(f"{student['name']},{student['age']},{student['grade']}\n")
    pass


# 测试
students = [
    {"name": "张三", "age": 20, "grade": "A"},
    {"name": "李四", "age": 19, "grade": "B"},
    {"name": "王五", "age": 21, "grade": "A"}
]

filename = "students.txt"

# 写入文件
write_students_to_file(students, filename)

# 读取文件
read_students = read_students_from_file(filename)
print("读取的学生信息：")
for student in read_students:
    print(student)

# 追加新学生
new_student = {"name": "赵六", "age": 22, "grade": "B"}
append_student_to_file(new_student, filename)

# 再次读取
read_students = read_students_from_file(filename)
print("\n追加后的学生信息：")
for student in read_students:
    print(student)