def calculator(operation, a, b):
    """
    计算器函数

    Args:
        operation (str): 运算类型 ('+', '-', '*', '/')
        a (float): 第一个数
        b (float): 第二个数

    Returns:
        float: 计算结果
    """
    # 你的代码：
    result = 0
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        return a / b
    pass


# 测试
print(calculator('+', 10, 5))  # 15
print(calculator('-', 10, 5))  # 5
print(calculator('*', 10, 5))  # 50
print(calculator('/', 10, 5))  # 2.0