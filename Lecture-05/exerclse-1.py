def is_armstrong(number):
    num_str = str(number)
    digits = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** digits
    return total == number

print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(123))