armstrong_numbers = []
for number in range(1,1001):
    digits  = []
    temp = number
    while temp > 0:
        digit = temp % 10
        digits.append(digit)
        temp //= 10
    total = 0
    for a in digits[::-1]:
        total += a**3
    if total == number:
        armstrong_numbers.append(number)
print(armstrong_numbers)