user_input = input("Enter a math expression: ")
result = eval(user_input)  # Unsafe! Runs any Python code passed by the user.
print(result)
