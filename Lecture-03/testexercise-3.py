number = int(input("Enter the number: "))
hourly = int(input("Enter the horly: "))

pay = (40 * hourly) + ((number - 40) * hourly * 1.5)

print("The gross pay is " , pay)

