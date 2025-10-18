# 任务：创建一个安全的除法函数
# 处理除零错误和类型错误

def safe_divide(a, b):
    """
    安全的除法函数

    Args:
        a: 被除数
        b: 除数

    Returns:
        除法结果或错误信息
    """
    # 你的代码：
    try:
        return a/b
    except ZeroDivisionError:
        return "除数不能为零"
    except TypeError:
        return "参数类型不正确"
    except Exception as e:
        return f"未知错误：{e}"
    pass


# 测试
print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # 错误：除数不能为零
print(safe_divide(10, "a"))  # 错误：参数类型不正确