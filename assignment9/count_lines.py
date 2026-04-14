def count_non_blank_lines(filename):
    count = 0
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() != "":
                count += 1
    return count

filename = "input1.txt"
result = count_non_blank_lines(filename)
print(result)