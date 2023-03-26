def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result
print(multiply_numbers(2, 3, 4, 5)) # выведет 120
print(multiply_numbers(1, 2, 3, 4, 5, 6)) # выведет 720


def mirror(text):
    return text[::-1]
text = "beatiful, day!"
mirrored_text = mirror(text)
print(mirrored_text)  # вывод   ит "!yad ,lufitaeb"