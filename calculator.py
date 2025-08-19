import math

def display_menu():
    """نمایش منوی انتخاب عملیات"""
    print("\n--- 🧮 Python Calculator ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (x ^ y)")
    print("6. Square Root (√x)")
    print("7. Logarithm (log₁₀)")
    print("8. Natural Log (ln)")
    print("9. Exit")


def get_number(prompt):
    """دریافت عدد از کاربر با مدیریت خطا"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number!")


def get_choice():
    """دریافت انتخاب کاربر با محدوده معتبر"""
    while True:
        try:
            choice = int(input("Choose an operation (1-9): "))
            if 1 <= choice <= 9:
                return choice
            else:
                print("❌ Please choose a number between 1 and 9.")
        except ValueError:
            print("❌ Please enter a number!")


def calculate(num1, num2, operation):
    """انجام محاسبه و بازگرداندن نتیجه"""
    if operation == 1:
        return num1 + num2
    elif operation == 2:
        return num1 - num2
    elif operation == 3:
        return num1 * num2
    elif operation == 4:
        if num2 == 0:
            raise ValueError("Cannot divide by zero!")
        return num1 / num2
    elif operation == 5:
        return math.pow(num1, num2)  # x ^ y
    elif operation == 6:
        if num1 < 0:
            raise ValueError("Cannot calculate square root of a negative number!")
        return math.sqrt(num1)
    elif operation == 7:
        if num1 <= 0:
            raise ValueError("Logarithm undefined for zero or negative numbers!")
        return math.log10(num1)
    elif operation == 8:
        if num1 <= 0:
            raise ValueError("Natural log undefined for zero or negative numbers!")
        return math.log(num1)
    else:
        return None


def get_symbol(choice, num1=None, num2=None):
    """بازگرداندن نماد مناسب برای نمایش عملیات"""
    symbols = {
        1: "+",
        2: "-",
        3: "*",
        4: "/",
        5: "^",
        6: "√",
        7: "log",
        8: "ln"
    }
    symbol = symbols.get(choice, "?")

    # برای عملیات تک‌متغیره، قالب خاصی تعریف می‌کنیم
    if choice in [6, 7, 8]:
        return f"{symbol}({num1})"
    else:
        return f"{num1} {symbol} {num2}"


def main():
    print("🚀 Welcome to the Advanced Python Calculator!")
    print("You can perform basic and advanced math operations.")

    while True:
        display_menu()
        choice = get_choice()

        if choice == 9:
            print("👋 Goodbye! Thanks for calculating with Python.")
            break

        # برای عملیات‌هایی که فقط به یک عدد نیاز دارند
        if choice in [6, 7, 8]:  # جذر، لگاریتم، لگاریتم طبیعی
            num = get_number("Enter the number: ")
            try:
                result = calculate(num, 0, choice)
                expression = get_symbol(choice, num1=num)
                print(f"✅ Result: {expression} = {result}")
            except ValueError as e:
                print(f"❌ Error: {e}")

        # برای عملیات دو متغیره
        else:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            try:
                result = calculate(num1, num2, choice)
                expression = get_symbol(choice, num1=num1, num2=num2)
                print(f"✅ Result: {expression} = {result}")
            except ValueError as e:
                print(f"❌ Error: {e}")


# اجرای برنامه
if __name__ == "__main__":
    main()
