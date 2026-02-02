# =========================
# EXERCÍCIO 1
# Trabalhando com:
# - lista de dicionários
# - lambda com closure
# - cálculo de imposto
# - sorted com lambda
# =========================

products = [
    {"name": "Keyboard", "price": 100, "tax": 0.10},
    {"name": "Mouse", "price": 50, "tax": 0.05},
    {"name": "Monitor", "price": 800, "tax": 0.15}
]

# Percorre os produtos exibindo o preço original
for item_price in products:
    print('preço antigo', item_price['name'], item_price['price'])

    # Closure com lambda:
    # price fica fixo e tax é aplicado depois
    calculate_taxes = (lambda price: lambda tax: price + (price * tax))(item_price["price"])

    # Atualiza o preço com imposto
    item_price['price'] = calculate_taxes(item_price['tax'])

# Ordena os produtos pelo novo preço
order_price = sorted(products, key=lambda value: value["price"])

# Exibe os produtos ordenados
for i, item in enumerate(order_price):
    print(i, item)


# =========================
# EXERCÍCIO 2
# Trabalhando com:
# - função que executa outra função
# - lambda + closure
# - aumento percentual
# =========================

products = [
    {"name": "Keyboard", "price": 100},
    {"name": "Mouse", "price": 50},
    {"name": "Monitor", "price": 800}
]

# Função genérica que executa outra função
def list_product(function, *args):
    return function(*args)

# Aplica aumento de 10% usando lambda e closure
for product in products:
    taxs = list_product(
        lambda product: lambda tax: product + (product * tax),
        product["price"]
    )
    print(f'{product["name"]} {taxs(10 / 100)} aumento 10%')


# =========================
# EXERCÍCIO 3
# Trabalhando com:
# - desempacotamento de variáveis
# - operador *
# =========================

a, a1, b, b1, *_ = 1, 2, 3, 4, 5, 6, 7, 8
print(a + a1, *_)


# =========================
# EXERCÍCIO 4
# Trabalhando com:
# - dicionários
# - unpacking
# - items()
# =========================

pessoa = { 
    'nome': 'adrian',
    'sobrenome': 'moises'
}

pessoa1 = { 
    'nom1e': 'adrian',
    'sobren1ome': 'moises'
}

# Desempacotando pares chave/valor
(a, a1), (b, b2) = pessoa.items()
print(a, b2, b, a1)

# Iterando sobre dicionário
for key, value in pessoa.items():
    print(key, value)

# Merge de dicionários com **
dic3 = {**pessoa1, **pessoa}
print(dic3)


# =========================
# EXERCÍCIO 5
# Trabalhando com:
# - *args
# - **kwargs
# =========================

def argumentos(*args, **kwargs):
    for key in args:
        print('nao nomeados', key)
    for key, value in kwargs.items():
        print(key, value)

# Passando dicionário como kwargs
argumentos(**dic3)


# =========================
# EXERCÍCIO 6
# Trabalhando com:
# - função de ordem superior
# - lambda
# - closure
# =========================

lista = []

# Função que executa qualquer função
def excuta(funcao, *args):
    return funcao(*args)

# Closure para saudação
greeting_function = excuta(
    lambda greet: lambda name: greet + name,
    'Good morning, '
)

# Closure para cálculo de imposto
taxes = excuta(
    lambda value_product: lambda tax_value: value_product + (value_product * tax_value),
    20
)

# Usando lambda para adicionar valores a uma lista
ordem = excuta(lambda *args: lista.append(list(args)), 4, 5, 2, 4, 5)

# Ordenando a lista criada
lista[0].sort()
print(lista)

print(f'com taxa valor é {taxes(10 / 100)}\n')
print(greeting_function('Adrian'))


# =========================
# EXERCÍCIO 7
# Trabalhando com:
# - funções normais
# - closure
# - lambda
# =========================

def soma(x, y):
    return x + y

# Closure clássica
def creat_multiplicador(multi):
    def multiplica(numero):
        return multi * numero
    return multiplica

oi = creat_multiplicador(5)

print(
    excuta(lambda multi, numero: multi * numero, 5, 10),
)

# Closure usando lambda
duplica = excuta(lambda m: lambda n: n * m, 5)
print(duplica(2))

# Closure para concatenação de string
elogio = excuta(lambda m: lambda n: m + n, 'adrian, ')
print(elogio('bunito'))

print(
    excuta(soma, 1, 2),
    soma(2, 3),
    excuta(lambda x, y: x + y, 1, 2)
)

exit()


# =========================
# EXERCÍCIO 8
# Trabalhando com:
# - sorted
# - lambda
# - lista de dicionários
# =========================

people = [
    {"name": "Carlos", "age": 30},
    {"name": "Ana", "age": 22},
    {"name": "Bruno", "age": 25},
    {"name": "Daniela", "age": 28}
]

def orden_age(list_age):
    for age in list_age:
        print(age)

# Ordenando por idade
age_old = sorted(people, key=lambda old: old["age"])
orden_age(age_old)

for name in people:
    print(name)

exit()


# =========================
# EXERCÍCIO 9
# Trabalhando com:
# - sorted com múltiplas chaves
# =========================

students = [
    {"name": "Lucas", "grade": 8.0},
    {"name": "Ana", "grade": 9.5},
    {"name": "Pedro", "grade": 8.0},
    {"name": "Marina", "grade": 7.5}
]

def exibir(list_):
    for studants_grades in list_:
        print(studants_grades)

# Ordena por nota e depois por nome
grade = sorted(students, key=lambda studant: (studant["grade"], studant["name"]))
exibir(grade)

exit()


# =========================
# EXERCÍCIO 10
# Trabalhando com:
# - ordenação por campos diferentes
# =========================

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def exibir(lista):
    for name in lista:
        print(name)
    print()

# Ordenação por nome
l1 = sorted(lista, key=lambda name: name['nome'])

# Ordenação por sobrenome
l2 = sorted(lista, key=lambda name: name['sobrenome'])

exibir(l1)
exibir(l2)


# =========================
# EXERCÍCIO 11
# Trabalhando com:
# - lambda
# - closure
# - cálculo de imposto
# =========================

lista = [
    {'ID': 0, 'Name': 'mause', 'price': 38.5, 'tax': 10.0},
    {'ID': 0, 'Name': 'mause', 'price': 33.5, 'tax': 10.0},
    {'ID': 0, 'Name': 'mause', 'price': 34.5, 'tax': 10.0}
]

def executa(fuction, *args):
    return fuction(*args)

# Aplica imposto usando closure
for item in lista:
    tax_product = executa(
        lambda price: lambda tax: price + (tax * price),
        item['price']
    )
    print(tax_product(item['tax'] / 100))

# Closure para saudação
greeting = executa(lambda greet: lambda name: greet + name, 'Good morning, ')
print(greeting('Adrian'))
