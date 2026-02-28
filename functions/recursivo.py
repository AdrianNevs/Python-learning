# usando def recursivo para contador
def recursivo(n):
    if n == 10:
        return n
    n += 1
    return recursivo(n)
n = 0
print(recursivo(n))



#exercicio 1 Faça a função parar em qualquer número N passado pelo usuário com limit 1500: 
import sys
sys.setrecursionlimit(1504)
def recursivo_par(n=0,l=None,end_user=None):
    if l is None:
        l = []

    if end_user is None or end_user <= 1:
        while True:
            try:
                end_user = int(input('Digite até quando vc quer: '))
                if end_user > 1 and end_user <= 1500:
                    break
                print('Digite > 1 and <= 1500:')
            except ValueError:
                print('apenas numeros int')
    n += 1
    if n % 2 == 0:
        l.append(n)        
    if n == end_user:
        return l
    return recursivo_par(n,l,end_user)

print(recursivo_par(end_user=1))


# recursivo factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(4))
