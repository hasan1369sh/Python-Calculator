def display_menu():
    """نمایش منوی انتخاب عملیات"""
    print("\n--- Calculator Menu ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")


def get_number(prompt):
    """دریافت عدد از کاربر با مدیریت خطا"""
    while True:
        try:
            return float(input(prompt))  # float برای اعشار هم کار کنه
        except ValueError:
            print("❌ Please enter a valid number!")


def get_choice():
    """دریافت انتخاب کاربر با مدیریت خطا"""
    while True:
        try:
            choice = int(input("Choose an operation (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("❌ Please choose a number between 1 and 5.")
        except ValueError:
            print("❌ Please enter a valid number!")


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
    else:
        return None


def main():
    print("🧮 Welcome to the Python Calculator!")

    while True:
        display_menu()
        choice = get_choice()

        if choice == 5:
            print("👋 Goodbye!")
            break

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            result = calculate(num1, num2, choice)
            print(f"✅ Result: {num1} {get_symbol(choice)} {num2} = {result}")
        except ValueError as e:
            print(f"❌ Error: {e}")


def get_symbol(choice):
    """بازگرداندن نماد عملیات برای نمایش زیباتر"""
    symbols = {1: "+", 2: "-", 3: "*", 4: "/"}
    return symbols.get(choice, "?")


# اجرای برنامه
if __name__ == "__main__":
    main()
