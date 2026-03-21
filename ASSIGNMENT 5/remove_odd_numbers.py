def remove_odd(numbers):
    return [num for num in numbers if num % 2 == 0]

# Main program
nums = [1, 2, 3, 4, 5, 6, 7, 8]
filtered = remove_odd(nums)

print("Original list:", nums)
print("Even numbers only:", filtered)