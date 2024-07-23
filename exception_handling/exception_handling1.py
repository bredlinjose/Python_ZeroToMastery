a = 5
b = 0

try:
    print("File open")
    k = int(input("Enter a number: "))
    print("Number is", k)
    print(a/b)  # ZeroDivisionError: division by zero
except ZeroDivisionError as e:
    print("HEY, YOU CANNOT DIVIDE A NUMBER BY ZERO", e)
except ValueError as e:
    print("INVALID INPUT", e)  # invalid literal for int() with base 10:
except Exception as e:
    print("SOMETHING WENT WRONG", e)
finally:
    print("File close")
