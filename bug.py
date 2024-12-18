def calculate_average(numbers):
    if not numbers:  # Check for empty list
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage
my_numbers = [10, 20, 30, 40, 50]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list) #This will return 0 as expected
print(f"The average of an empty list is: {result}")

my_numbers2 = [10,20, 'a']
result = calculate_average(my_numbers2) # This will throw an error because it tries to sum a string