def calaulate_stats(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total_sum, average, maximum, minimum

numbers = [5, 10, 15, 20, 25]
total, avg, max_num, min_num = calaulate_stats(numbers)

print(f"Total Sum: {total}")
print(f"average: {avg}")
print(f"Maximum: {max_num}")
print(f"Minimun: {min_num}")