def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    Args:
        numbers (list): A list of numeric values.
    Returns:
        float: The average of the input numbers, or 0.0 if the list is empty.
    """
    # Перевірка на порожній список (уникаємо ділення на нуль)
    if not numbers:
        return 0.0

    # Використовуємо вбудовані функції для швидкості та читабельності
    average = sum(numbers) / len(numbers)
    return average


# Приклади використання
print(f"Середнє (звичайний список): {calculate_average([10, 20, 30, 40, 50])}")
print(f"Середнє (порожній список): {calculate_average([])}")