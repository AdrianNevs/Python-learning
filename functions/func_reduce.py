from functools import reduce
# ======================================
# INTRODUÇÃO AO REDUCE
# ====================================
#primeiro passos
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

# ======================================
# Exercícios aprendendo a usar o reduce
# ======================================
#Faça um programa que leia números inteiros m e n e os elementos de uma matriz A de números 
#inteiros de dimensão m x n e conte o número de elementos que são iguais a zero utilizando reduce

m = int(input('Informe a quantidade de linhas (m): '))
n = int(input('Informe a quantidade de colunas (n): '))
matriz_numbers = [[int(input(f'Digite o elemento [{i}][{j}]: ')) for j in range(n)] for i in range(m)] # Criação da matriz List Comprehension

def count_zero(accumulate,matriz):
    zero = matriz.count(0)
    return accumulate + zero
    
reduce_zero = reduce(count_zero,matriz_numbers,0)
print('Quantidade de zeros',reduce_zero)

#=====================================
#forma mais profissional e facil de dbugar:
def count_zero(accumulate,matriz):
    zero = reduce(lambda acc,value: acc + 1 if value == 0 else acc,matriz,0)
    return accumulate + zero
    
reduce_zero = reduce(count_zero,matriz_numbers,0)
print('Quantidade de zeros',reduce_zero)



#/////////////=====================================\\\\\\\\\\\\\\\\
#/////////////=====================================\\\\\\\\\\\\\\\\
# line_matriz pega cada linha da matriz.
# acc é o acumulador geral (contador total principal), iniciado em 0.
# Para cada linha, o reduce interno conta quantos valores iguais a 1 existem.
# value_line representa cada elemento dentro da linha atual.
# zero_count é o acumulador da linha, responsável por somar os valores encontrados.
# O operador ternário adiciona 1 ao contador quando o valor é 1,
# caso contrário adiciona 0, mantendo o valor atual.
# O resultado do reduce interno (quantidade de 1 na linha)
# é somado ao acc no reduce externo.
# No final, definimos a matriz que será percorrida e o valor inicial do acumulador.
# imagine como se primeiro reduce fosse um for i ,
# eo segundo fosse reduce fosse o for j 
count_one = reduce(lambda acc,line_matriz:acc + reduce(lambda zero_count,value_line: zero_count + (1 if value_line == 1 else 0),line_matriz,0),matriz_numbers,0) 
print('quantidade de 1 = ',count_one)


#/////////////=====================================\\\\\\\\\\\\\\\\
#/////////////=====================================\\\\\\\\\\\\\\\\
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
