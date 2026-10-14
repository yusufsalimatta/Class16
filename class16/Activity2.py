try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("Result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except SyntaxError:
    print("comma is Missing. Enter numbers separated by a comma like 1, 2")


except :
    print("Wrong input.")


else:
    print("No exception occurred.")

finally:
    print("This Will always execute.")