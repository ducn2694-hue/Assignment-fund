numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    
    if user_input == "":
        break
    
    numbers.append(float(user_input))

numbers.sort(reverse=True)

print("Top 5 greatest numbers:")
print(numbers[:5])