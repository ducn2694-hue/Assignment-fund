def calculate_average_score(filename):
    total_score = 0
    total_students = 0

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip() != "":
                name, score = line.strip().split(",")
                total_score += float(score)
                total_students += 1

    if total_students == 0:
        return 0
    else:
        return total_score / total_students

filename = "scores.txt"
result = calculate_average_score(filename)
print(result)