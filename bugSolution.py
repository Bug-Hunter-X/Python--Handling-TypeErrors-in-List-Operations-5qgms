def calculate_average(numbers):
    try:
        if not numbers:
            return 0
        total = sum(numbers)
        average = total / len(numbers)
        return average
    except TypeError:
        print("Error: List must contain only numbers.")
        return None

# Example usage
my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average of an empty list is: {result}")

my_numbers2 = [10, 20, 'a']
result = calculate_average(my_numbers2) # This will print an error message now instead of crashing
print(f"The average is: {result}")
