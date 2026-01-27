# exercicio 1
limit = 10

def count_up_to(n=0,maximum=limit):
    while True:
        n += 1
        yield n
        if n >= maximum:
            return
        

limit = count_up_to()
for n in limit:
    print(n)


#maneira mais facil
def count_up_to(n=1,maximum=limit):
    for n in range(n,maximum + 1):
        yield n
        

limit = count_up_to()
for n in limit:
    print(n)



# exercicio 2
def even_number(n=0 , maximum=10):
    while True:
        n += 1
        if n % 2 == 0:
            yield f'Par {n}'
        if n >= 10:
            return
        
for value in even_number(maximum=10):
    print(value)



#exercicio 3

def square_numbers(numbers):
    for value in numbers:
        yield value ** 2

numbers = [2, 3, 4]

even = square_numbers(numbers)
for value in even:
    print(value)

