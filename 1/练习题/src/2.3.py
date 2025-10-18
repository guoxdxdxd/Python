# 任务：打印九九乘法表
# 格式如下：
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 9 x 9 = 81

def print_multiplication_table():
    # 你的代码：
    for i in range(1, 10):
        line = ""
        for j in range(1, 10):
            item = ""
            if j >= i :
                item = f"{i} x {j} = {i * j}  "
            else :
                item = "           "
            line += item.ljust(12)
        print (line)
    pass

# 调用函数
print_multiplication_table()