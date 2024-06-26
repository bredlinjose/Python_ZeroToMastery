user_name = input("Username: ")
password = input("Password: ")

password_length = len(password)
hidden_password = '*' * password_length

print(f'{user_name} your password {hidden_password}, is {password_length} letters long')
