from functools import reduce
products = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
#com comprehension
total = [ p['preco'] for p in products]
print(sum(total))

#quase na unha
value = 0
for p in products:
    value += p['preco']
print(value)

# na unha
value_total = 0
for i in range(len(products)):
    value_total += products[i]['preco']
print(value_total)

#usando reduce
def func_reduce(accumulate,product):
    return accumulate + product['preco']

total = reduce(
    func_reduce,products,
    0
)
print(total)

#/////////////=====================================\\\\\\\\\\\\\\\\
#/////////////=====================================\\\\\\\\\\\\\\\\
#exercicios aprededo a usar o reduce 
#Exercício 1
#Crie uma função com reduce que receba uma lista de números
#e retorne a soma apenas dos números pares.
def sum_pair(accumulate,values):
    return accumulate + values if values % 2 == 0 else accumulate

list_numbers = range(10)
total_sum = reduce(sum_pair,list_numbers,0)

print(total_sum)
#/////////////=====================================\\\\\\\\\\\\\\\\
#ex 2 usando lambda e reduce
creat_sum = reduce((lambda accumulate,
                  value:accumulate + value if value % 2 == 0 else accumulate),
                  list_numbers,
                  0)
print(creat_sum)
#/////////////=====================================\\\\\\\\\\\\\\\\
#Exercício 2 — Total do carrinho (com quantidade)
# Você tem uma lista de produtos:
# Crie um reduce que calcule:
# valor total do carrinho
# (price * quantity).

products = [
     {"name": "mouse", "price": 50, "quantity": 2},
     {"name": "keyboard", "price": 120, "quantity": 1},
     {"name": "monitor", "price": 900, "quantity": 1},
 ]


def price_sum(accumulate,value):
    return accumulate + (value['price'] * value['quantity'])

total_products = reduce(price_sum,products,0)
print(total_products)
#/////////////=====================================\\\\\\\\\\\\\\\\
#usado lambda

total_multi = reduce((lambda accumulate,value:
                    accumulate + value['price'] * value['quantity'])
                    ,products,0
)
print(total_multi)
#/////////////=====================================\\\\\\\\\\\\\\\\
# Exercício 3 — Encontrar o maior preço
# Use reduce para retornar o produto mais caro
products = [
    {"name": "mouse", "price": 50},
    {"name": "keyboard", "price": 120},
    {"name": "monitor", "price": 900},
]

def larger_value(accumulate,dic_products):
    if accumulate['price'] < dic_products['price']:
        return dic_products
    return accumulate

larger = reduce(larger_value,products)
print(larger)
