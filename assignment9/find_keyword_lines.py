def find_keyword_lines(filename, keyword):
    line_numbers = []
    with open(filename, "r", encoding="utf-8") as file:
        line_number = 1
        for line in file:
            if keyword in line:
                line_numbers.append(line_number)
            line_number += 1
    return line_numbers


filename = "input2.txt"
keyword = "hello"
result = find_keyword_lines(filename, keyword)
print(result)