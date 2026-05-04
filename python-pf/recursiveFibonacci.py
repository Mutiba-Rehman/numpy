def fib(n):
# base case (stopping condition)
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    

# the above function only returns a single fibonacci term
# for the sake of printing series, we're using loop

for i in range(10):
    print(fib(i))