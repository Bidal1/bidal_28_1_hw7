def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply_numbers(2, 3, 4, 5)) # выведет 120
print(multiply_numbers(1, 2, 3, 4, 5, 6)) # выведет 720


def is_palindrome(string, hello='hello'):
    if string == string[::-1]:
        return True
    elif string == hello:
        return "This is 'hello'"
    else:
        return False


print(is_palindrome('racecar')) # True
print(is_palindrome('hello')) # This is 'hello'
print(is_palindrome('world')) # False

def calculator(num1, operator, num2):

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Ошибка: деление на ноль!"
        else:
            return num1 / num2
    elif operator == "**":
        return num1 ** num2
    elif operator == "%":
        return num1 % num2
    elif operator == "//":
        if num2 == 0:
            return "Ошибка: деление на ноль!"
        else:
            return num1 // num2
    else:
        return "Ошибка: неизвестный оператор!"
result = calculator(2, "**", 3)
print(result)  # выводит 8

result = calculator(5, "+", 9.6)
print(result)  # выводит 14.6

result = calculator(20, "%", 3)
print(result)  # выводит 2

result = calculator(10, "/", 0)
print(result)  # выводит "Ошибка: деление на ноль!"

result = calculator(7, "^", 8)
print(result)  # выводит "Ошибка: неизвестный оператор!"