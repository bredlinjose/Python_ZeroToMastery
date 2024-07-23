a = 5
b = 0

try:
    print("File open")
    print(a/b)  # ZeroDivisionError: division by zero
except Exception as e:
    print("HEY, YOU CANNOT DIVIDE A NUMBER BY ZERO", e)
finally:
    print("File close")
