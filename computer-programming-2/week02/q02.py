fibonacci_list = [0,1]
number = int(input("Lütfen Fibonacci için sayı giriniz:"))
for i in range(2,number+1):
    total = fibonacci_list[-1] + fibonacci_list[-2]
    fibonacci_list.append(total)
print(fibonacci_list)