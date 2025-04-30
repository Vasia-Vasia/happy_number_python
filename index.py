def sum_of_square_digits(number):
    result = 0
    for number in str(number):
        square = int(number) ** 2
        result = result + square
    return result


def is_happy_number(number):
    i = 1
    while i <= 10:
        number = sum_of_square_digits(number)
        i = i + 1

    if number == 1:
        return True
    else:
        return False

# Проверка

number = 7
print(is_happy_number(number))