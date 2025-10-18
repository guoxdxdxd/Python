# 测试数据
numbers = [1, 2, 3, 4, 5]
strings = ["hello", "world", "python"]

# 1. 计算平方
square = lambda x: x ** 2
squares = list(map(square, numbers))
print(f"平方：{squares}")

# 2. 判断是否为偶数
is_even = lambda x: x % 2 == 0
even_numbers = list(filter(is_even, numbers))
print(f"偶数：{even_numbers}")

# 3. 获取字符串长度
get_length = lambda s: len(s)
lengths = list(map(get_length, strings))
print(f"长度：{lengths}")