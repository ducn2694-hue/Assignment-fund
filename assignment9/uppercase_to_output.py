def convert_file_to_uppercase(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    content = content.upper()

    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(content)


filename = "input3.txt"
convert_file_to_uppercase(filename)
print("Done")
