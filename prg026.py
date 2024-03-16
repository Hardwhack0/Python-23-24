def find_odd_numbers(start, end):
    odd_numbers = [num for num in range(start, end+1) if num % 2 != 0]
    return odd_numbers

start_range = 1
end_range = 20
odd_numbers_in_range = find_odd_numbers(start_range, end_range)
print(f"Odd numbers in the range {start_range} to {end_range} are: {odd_numbers_in_range}")