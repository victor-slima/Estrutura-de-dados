def fat(n):
    if n == 1:
        return 1
    else:
        return n * fat(n-1)

print(fat(13))

# multiplicacao e exponenciacao tambem sao exemplos

def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))