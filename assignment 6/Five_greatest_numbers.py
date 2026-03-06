numbers = []

while True:
    n = input("Enter number: ")

    if n == "":
        break

    numbers.append(int(n))

numbers.sort(reverse=True)

print("Five greatest numbers:")
for num in numbers[:5]:
    print(num)