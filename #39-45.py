#39
def print_n (n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)
            
num = int(input("양수를 입력하세요: "))

if num > 0:
    print_n(num)
else:
    print("양수를 입력하세요: ")
    
#40
def print_a(n):
        if n % 3 == 0:
            print(n)
            
num = int(input("숫자를 입력하세요: "))
print_a(num)

#41
def max_min(a, b, c, d):
    maximum = max(a, b, c, d)
    minimum = min(a, b, c, d)
    return maximum, minimum

n1 = int(input("첫 번째 숫자를 입력하세요: "))
n2 = int(input("두 번째 숫자를 입력하세요: "))
n3 = int(input("세 번째 숫자를 입력하세요: "))
n4 = int(input("네 번째 숫자를 입력하세요: "))

max_value, min_value = max_min(n1, n2, n3, n4)

print("최댓값: ", max_value)
print("최솟값: ", min_value)

#42
def print_n (n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)
            
num = int(input("양수를 입력하세요: "))

if num > 0:
    print_n(num)
else:
    print("양수를 입력하세요: ")
    
#43
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n= int(input("0이상의 정수를 입력하세요: "))

if n >= 0:
    print(factorial(n))
    
#44
def sum_over_30(i, j):
    total = 0
    for a in range(1, i + 1):
        for b in range(j, j + 1):
            if a * b >= 30:
                total += a * b
    return total

i = int(input("2이상 9이하의 첫 번째 수(i)를 입력하세요: "))
j = int(input("2이상 9이하의 첫 번째 수(j)를 입력하세요: "))

if 2 <= i <= 9 and 2 <= j <= 9:
    result = sum_over_30(i, j)
    print(result)
    
#45
def sum_list(values):
    total = 0
    for v in values:
        total += v
    return total

a = [1, 2, 3, 4, 5]

result = sum_list(a)
print(result)