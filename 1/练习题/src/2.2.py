# 任务：计算 1 到 100 的和
# 使用 for 循环和 while 循环分别实现

# 方法1：for 循环
def sum_with_for():
    # 你的代码：
    total = 0
    for i in range(1, 101):
        total += i
    return total

# 方法2：while 循环
def sum_with_while():
    # 你的代码：
    total = 0
    i = 1
    while i <= 100:
        total += i
        i += 1
    return total

# 测试
print(f"for 循环结果：{sum_with_for()}")
print(f"while 循环结果：{sum_with_while()}")