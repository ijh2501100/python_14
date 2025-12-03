# python_14
# Python GitHub 과제

## 1. 과제 개요
- user-defined function을 이용한 파이썬 코드
---

## 2. 수행 과정
#39 사용자로부터 양수(숫자)를 입력받아서, 0부터 해당 숫자포함까지 홀수를 출력. 단 user-defined function를 이용
def print_n (n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)
            
num = int(input("양수를 입력하세요: "))

if num > 0:
    print_n(num)
else:
    print("양수를 입력하세요: ")
    
#40 사용자로부터 숫자를 입력받아서 3의 배수일때만 출력. 단 user-defined function를 이용
def print_a(n):
        if n % 3 == 0:
            print(n)
            
num = int(input("숫자를 입력하세요: "))
print_a(num)

#41 사용자로부터 숫자 4개를 입력받은 후, 최댓값과 최솟값을 계산. 단 user-defined function를 이용하고 함수의 매개변수는 점수 4개를 받고, 최댓값과 최솟값을 리턴
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

#42 사용자로부터 양수(숫자)를 입력받아서, 0부터 해당 숫자포함까지 홀수를 출력. 단 user-defined function를 이용
def print_n (n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            print(i)
            
num = int(input("양수를 입력하세요: "))

if num > 0:
    print_n(num)
else:
    print("양수를 입력하세요: ")

#43 사용자로부터 0보다 크거나 같은 정수 n을 입력받아 n! (펙토리얼)을 계산해서 출력. 단 user-defined function를 이용
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n= int(input("0이상의 정수를 입력하세요: "))

if n >= 0:
    print(factorial(n))

#44 사용자로부터 2이상 9이하의 양수(숫자) 2개 j)를 입력받아서, 이중반복문을 돌면서 1와 j의 곱이 30 이상인 경우의 총 합을 출력. 단 user-defined function를 이용
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

#45 a=[1, 2, 3, 4, 5] 리스트를 함수의 입력으로 받아서 리스트 값의 누적 합을 출력. 단 user-defined function를 이용
def sum_list(values):
    total = 0
    for v in values:
        total += v
    return total

a = [1, 2, 3, 4, 5]

result = sum_list(a)
print(result)
---

## 3. GitHub Repository URL
- URL: [https://github.com/ijh2501100/python_14.git]
---
