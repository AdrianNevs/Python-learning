
exit()
#exercicio 1
def multipliar(multiple):
    def calculo(number):
        return multiple * number
    return calculo

two = multipliar(2)

for number in [1,2,3]:
    print(f'{two(number)}')

#exercicio 2

def greeting(greet):
    def return_name(name):
        return f'{greet} , {name}!'
    return return_name

return_gdmorning = greeting('Good morning')

for name in ['Lorena','Adrian']:
    print(return_gdmorning(name))

#exercicio 3

def percentage(discount):
    def product(value):
        return value - (value * (discount / 100))
    return product

discount_10 = percentage(10)
discount_20 = percentage(10)

for price in [100,200,300]:
    print(f'value of product no discount {price}')
    print(f'value of product with discount {discount_10(price)}')

# 4 exercicio

def tax(tax_value):
    def calculate(value_product):
        return value_product + tax_value
    return calculate

taxes = tax(15)
for product in [100,200,300]:
    print('as taxas sobre produtos sao 15 reias')
    print(f'produto valor {product} = {taxes(product)} valor final')

# 5 exercicio

def high(exponent):
    def calculate(number):
        return number ** exponent
    return calculate

number_expo = high(2)

for number in [1,2,3]:
    print(number_expo(number))

#6 exercicio 

def prefixo(msg_fixo):
    def user_msg(msg):
        return f'{msg_fixo} , {msg}!'
    return user_msg

fixo = prefixo('DEV')

print(fixo('Python'))

# 7 exercicio

def user(age_min):
    def verification(age):
        return True if age >= age_min else False
    return verification

age_min = user(18)

print(age_min(17))

# 8 exercicio

def taxes(value):
    def tax_calculate(number):
        return number * value
    return tax_calculate

tax = taxes(5)

print(tax(10))

#9 exercicio
def ask_number(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('digite numero inteiro')


def creat_sum(n1):
    def calculate_sum(n2):
        return n1 + n2
    return calculate_sum

sum_1 = ask_number('1 numero que deseja somar\nDigite:')
sum_2 = ask_number('2 numero que deseja somar\nDigite:')
sum_fuction = creat_sum(sum_1)
resultado = sum_fuction(sum_2)
print(f'resultado da soma é {resultado}')

# exercicio 10

def final_sentence(msg_final):
    def user_msg(msg):
        return f'{msg}, {msg_final}'
    return user_msg

final_msg = final_sentence('welcome')

for name in ['Adrian','Lorena']:
    print(final_msg(name))

#udemy

exit()
def create_multiplear(multipliar):
    def calculate(number):
        return f'{multipliar} x {number} = value is {multipliar * number}'
    return calculate

multiplir_one = create_multiplear(1)
multiplir_two = create_multiplear(2)

for number in [1,2,3]:
    print(multiplir_one(number))
    print(multiplir_two(number))


exit()
def create_greeting(greeting):
    def user(name):
        return f'{greeting}, {name}!'
    return user

return_goodmorning = create_greeting('good morning')

for name in ['adrian','lorena']:
    print(return_goodmorning(name))
exit()
def greeting(msg,name):
    return f'{msg}, {name}'

def execute(function,*args):
    return function(*args)


print(execute(greeting,'bom dia','Adrian'))

def multiplicar(*args):
    if len(args) == 0:
        return 'sem valores'
    fatorial = args[0]
    for i in range(len(args) - 1):
        fatorial = args[i + 1] * fatorial
        print(args[i] , args[i + 1])
        
    return fatorial

print(multiplicar())



def par_impar(numero):
    if numero % 2 != 0:
        return 'impar'
    return 'par'
print(par_impar(2))
def multiplicar(*args):

    if not args:
        return 'sem valores'

    resultado = 1
    for valor in args:
        resultado *= valor

    return resultado



exit()
