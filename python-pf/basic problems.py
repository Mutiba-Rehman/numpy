#factorial
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    print(f"Factorial of {num} is {fact}")


#Even Odd
def evenOdd(num):
    if num%2==0:
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

#Reversing a String
def strReverse(str):
    ans = str[ : :-1]
    return ans
   

def fibonacci(n):
    a,b = 0,1
    print(f"{a} {b}", end=" ")
    for i in range(n):
        c = a+b
        a=b
        b=c
        print(f"{c}", end=" ")

def palindrome(str):
    rev = strReverse(str)

    if str.lower() == rev.lower():
        print("Palindrome")
    else:
        print("Not Palindrome")

#Average of 5 numbers

def average(a,b,c,d,e):
    avg = float((a+b+c+d+e)/5)
    return avg

#cumulative sum of a range
def csum(num):
    sum = 0
    for i in range(num):
        sum+=i
    print(f"Cumulative sum is: {sum}")

#pattern

def tri(n):
    for i in range(n):
        for j in range(i):
            print(i, end=" ")
        print("")
#Number palindrome

def pal(num):
    num = str(num)
    if num[: : 1]==num[: : -1]:
        print("Palindrome")
    else:
        print("Not PAlindrome")

#Multi-Tiered Income Tax Calculation
#First 10000: 0%
#Next 10000: 10%
#Remaining Income: 20%
def tax(income):
    tax = 0
    if income <= 10000:
        print("No Tax")
    else:
        income-=10000
        tax+=(10000*(.10))
        income-=10000
        tax+=(income*(.20))
        print(tax)

# pattern
"""
* * * * *
* * * *
* * *
* *
*
"""

def star(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*", end=" ")
        print("")

star(5)