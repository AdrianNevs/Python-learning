# Exercícios práticos de Python focados em lógica, listas, dicionários,
# comprehension, funções,copy, lambda , sorted

#exercicio 1 sorted com lambda
numbers = [2, 5, 10, 3, 8]

order_number = sorted(numbers,key=lambda n:n, reverse=True)
print(order_number)

#exercicio 2 Use sorted com lambda para ordenar os produtos pelo price (crescente).

products = [
    {"name": "Keyboard", "price": 100},
    {"name": "Mouse", "price": 50},
    {"name": "Monitor", "price": 800}
]

order_price = sorted(products,key=lambda value:value['price'])
print(*order_price, sep='\n')

#exercicio 3 Crie uma nova lista contendo apenas os números pares.

numbers = [1, 2, 3, 4, 5, 6]

number_par = [value for value in numbers if value % 2 == 0]

print(number_par)

# exercicio 4 Crie duas lambda que receba dois números e retorne o maior deles.
def executa(fuction,*args):
    return fuction(*args)

bigger_number = executa(lambda x: lambda y:
                 f'maior x = {x} menor y = {y}' if x > y else f'maior y = {y} menor x = {x}' ,6)
print(bigger_number(3))

# 5 Crie uma nova lista com todos os preços aumentados em 10%.
prices = [10, 20, 30, 40]
tax = 10
tax_price = [ price + ((tax / 100) * price) for price in prices ]
print(tax_price)

#exercicio 6 Crie um novo dicionário apenas com os alunos que têm nota maior ou igual a 7.
students = {
    "Ana": 8,
    "Carlos": 5,
    "Maria": 9
}

media = [ {name:nota} for name,nota in students.items() if nota >= 7]

print(*media, sep='\n')

# sem funcao pronta ex 7 Crie uma função calculate_average(numbers) que receba uma lista de números e retorne a média.
def calculate_average(numbers):
    media = 0
    for number in numbers:
        media += number
    return media / len(numbers)

numbers_list = [3,2,3,2,3]

print(f'media dos valores = {calculate_average(numbers_list)}')

# ex 7 com funcao pronta

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

numbers_list = [3,2,3,2,3]

print(f'media dos valores = {calculate_average(numbers_list)}')


# exercicio 8  Crie uma função que retorne uma nova lista com o preço já com imposto aplicado.
products = [
    {"name": "Keyboard", "price": 100, "tax": 0.10},
    {"name": "Mouse", "price": 50, "tax": 0.05}
]

def calculate_tax(list_products):
    return [{**product, 'price':product['price'] + (product['price'] * product['tax'])} for product in list_products]
    
print(calculate_tax(products))
print(products)
    
# sem funcao pronta

def calculate_tax(list_products):
    lista_new = []
    for item in list_products:
        lista_new.append(item.copy())
    for item in lista_new:
        item['price'] = item['price'] + (item['price'] * item['tax'])
    return lista_new


print(calculate_tax(products))
print(products)
     
#9 final # sem comprehesion adicionar estoque no dicionario usando def 
products = [
    {"name": "Keyboard", "price": 100, "tax": 0.10},
    {"name": "Mouse", "price": 50, "tax": 0.05}
]

def creat_stock(products, amount):
    for item in products:
        item.update(stock=amount)
    return products


#ex 9 com comprehesion  criando nova lista nao alterando a original

def creat_stock(products,amount):
    return [{**item, 'stock': amount} for item in products]

print(creat_stock(products,10))
