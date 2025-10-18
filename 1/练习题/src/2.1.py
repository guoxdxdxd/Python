def get_grade(score):
    # 你的代码：
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    pass

# 测试
scores = [95, 85, 75, 65, 55]
for score in scores:
    grade = get_grade(score)
    print(f"分数：{score}，等级：{grade}")