# 任务：创建一个函数，计算多个数的平均值
# 支持可变参数

def calculate_average(*numbers):
    """
    计算多个数的平均值

    Args:
        *numbers: 可变数量的数字

    Returns:
        float: 平均值
    """
    # 你的代码：
    result = sum(numbers) / len(numbers)
    return result


# 测试
print(calculate_average(1, 2, 3, 4, 5))  # 3.0
print(calculate_average(10, 20, 30))  # 20.0
print(calculate_average(5))  # 5.0