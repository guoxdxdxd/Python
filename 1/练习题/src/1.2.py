text = "Hello, Python Programming!"
length = len(text)
print(F"长度：{length}")
print(F"大写：{text.upper()}")
print(F"小些：{text.lower()}")
print(F"替换：{text.replace("Python","Net")}")
print(F"分割：{text.split(', ')}")
first_five = text[0:5]
print(F"前5个字符：{first_five}")