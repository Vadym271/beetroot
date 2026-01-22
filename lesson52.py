from typing import Optional, Union

#task 1
def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    """
    Returns x ^ exp using recursion.
    """
    if exp <= 0:
        raise ValueError("This function works only with exp > 0.")

    if exp == 1:
        return x


    return x * to_power(x, exp - 1)

# task 2
def is_palindrome(looking_str: str) -> bool:
    if len(looking_str) <= 1:
        return True

    if looking_str[0] != looking_str[-1]:
        return False

    return is_palindrome(looking_str[1:-1])

#task 3
def mult(a: int, n: int) -> int:
    if n < 0:
        raise ValueError("This function works only with positive integers")

    if n == 0:
        return 0

    return a + mult(a, n - 1)

#task 4
def reverse(input_str: str) -> str:
    if len(input_str) <= 1:
        return input_str

    return input_str[-1] + reverse(input_str[:-1])

#task 5
def sum_of_digits(digit_string: str) -> int:
    if len(digit_string) == 0:
        return 0

    if not digit_string.isdigit():
        raise ValueError("input string must be digit string")

    return int(digit_string[0]) + sum_of_digits(digit_string[1:])

# Task 1
print(to_power(3.5, 2))      # Виведе: 12.25

# Task 2
print(is_palindrome("abba")) # Виведе: True

# Task 3
print(mult(5, 3))            # Виведе: 15

# Task 4
print(reverse("recursion"))  # Виведе: noisrucer

# Task 5
print(sum_of_digits("1234")) # Виведе: 10