from datetime import datetime


class CalculatorHistory:
    def __init__(self, time, history):
        self.time = time
        self.history = history


class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.add_history(datetime.now(),f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.add_history(datetime.now(),f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.add_history(datetime.now(),f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """除法"""
        if b == 0:
            raise ValueError("除数不能为零")
        result = a / b
        self.add_history(datetime.now(),f"{a} / {b} = {result}")
        return result

    def add_history(self, time, history):
        history_obj = CalculatorHistory(time, history)
        self.history.append(history_obj)

    def show_function_name(self):
        print("\n=== 计算器程序 ===")
        print("功能列表：")
        print("1. 加法")
        print("2. 减法")
        print("3. 乘法")
        print("4. 除法")
        print("5. 显示历史记录")
        print("6. 退出")
