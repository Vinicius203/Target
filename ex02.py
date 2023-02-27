n = int(input('Entre com um número: '))
fib0 = 0
fib1 = 1

check = False

while fib0 <= n:
    if n == fib0:
        check = True
        break
    fib0, fib1 = fib1, fib1 + fib0

if check == True:
    print(f'O número {n} pertence a sequência de Fibonacci.')
else:
    print(f'O número {n} NãO pertence a sequência de Fibonacci.')

