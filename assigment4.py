import re

def check_course_code(s):
    if re.fullmatch(r"[A-Z]{3}[0-9]{3}", s):
        return True
    else:
        return False


def check_hex_color(s):
    if re.fullmatch(r"#[0-9A-Fa-f]{6}", s):
        return True
    else:
        return False


def sum_numbers(text):
    numbers = re.findall(r"[0-9]+", text)
    total = 0
    for n in numbers:
        total += int(n)
    return total


def hide_phone_numbers(text):
    return re.sub(r"\+84[0-9]{9}|\b[0-9]{10}\b", "[REDACTED]", text)


print(check_course_code("TEC001"))
print(check_hex_color("#FFAACC"))
print(sum_numbers("Today is January 16, 2025. The temperature is 11 degrees Celsius."))
print(hide_phone_numbers("Call me at 0987654321 or +84987654321"))