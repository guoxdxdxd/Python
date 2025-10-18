fruits = ["苹果", "香蕉", "橙子"]
fruits.append("葡萄")
print(F"添加：{fruits}")
fruits.insert(1, "橘子")
print(F"插入：{fruits}")
fruits.remove("香蕉")
print(F"删除：{fruits}")
length = len(fruits)
print(F"长度：{length}")
has_apple = "苹果" in fruits
print(F"包含：{has_apple}")
fruits.reverse()
print(F"反转：{fruits}")