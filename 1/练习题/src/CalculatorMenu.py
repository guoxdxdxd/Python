from calculator import Calculator



def main():
    calc = Calculator()

    while True:
        calc.show_function_name()

        choice = input("请选择操作 (1-8): ")

        if choice == "1":
            a = float(input("请输入第一个数字: "))
            b = float(input("请输入第二个数字: "))
            result = calc.add(a, b)
            print(f"结果: {result}")
        elif choice == "2":
            a = float(input("请输入第一个数字: "))
            b = float(input("请输入第二个数字: "))
            result = calc.subtract(a, b)
            print(f"结果: {result}")
        elif choice == "3":
            a = float(input("请输入第一个数字: "))
            b = float(input("请输入第二个数字: "))
            result = calc.multiply(a, b)
            print(f"结果: {result}")
        elif choice == "4":
            a = float(input("请输入第一个数字: "))
            b = float(input("请输入第二个数字: "))
            result = calc.divide(a, b)
            print(f"结果: {result}")
        elif choice == "5":
            print("\n历史记录:")
            for history in calc.history:
                print(f"{history.time.strftime("%Y-%m-%d %H:%M:%S")}: {history.history}")
        elif choice == "6":
            print("已退出计算器程序。")
            break
        else:
            print("无效的选择，请重新输入。")

if __name__ == "__main__":
    main()