# 任务：创建自定义异常类
# 当年龄为负数时抛出异常

class NegativeAgeError(Exception):
    """年龄为负数的异常"""

    pass


def validate_age(age):
    """
    验证年龄

    Args:
        age: 年龄

    Raises:
        NegativeAgeError: 当年龄为负数时
    """
    # 你的代码：
    if age < 0:
        raise NegativeAgeError("年龄不能是负数")
    pass


# 测试
try:
    validate_age(25)
    print("年龄验证通过")
except NegativeAgeError as e:
    print(f"年龄验证失败：{e}")

try:
    validate_age(-5)
    print("年龄验证通过")
except NegativeAgeError as e:
    print(f"年龄验证失败：{e}")