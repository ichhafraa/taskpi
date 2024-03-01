import math

numbers = []
while True:
    num = int(input("Enter a number (-1 to stop): "))
    if num == -1:
        break
    numbers.append(num)

sum_numbers = sum(numbers)
print("Sum of numbers:", sum_numbers)