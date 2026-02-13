# Crie uma lambda que receba uma lista de números e retorne uma lista apenas com os números ímpares.

impares = lambda n: n % 2 != 0
numbers = [n for n in range(10) if impares(n)]
print(numbers)

# Crie uma lambda que receba dois números e retorne o menor deles.
# simples e facil
larger_value = lambda x, y: min(x,y)
print('menor valor = ',larger_value(10,20))
#simples e didatico com if ternario
larger_value = lambda x, y: f'menor x = {x}, maior y = {y}' if x < y else f'menor y = {y} maior x = {x}'
print(larger_value(10,20))

#Faça uma lista com os quadrados dos números pares de 1 a 10.

list_square = [n ** 2 for n in range(10) if n % 2 == 0]
print(list_square)

# Crie uma função que receba uma lista de preços e aplique 15% de imposto, retornando uma nova lista sem alterar a original.

def calculate_impost(list_number,tax):
    return [number + (number * (tax / 100)) for number in list_number]


list_values = list_square
tax = 10
print(calculate_impost(list_values,tax))
print(list_square)

#crie uma função que receba uma lista de nomes e retorne uma nova lista com os nomes em maiúsculas, sem alterar a lista original.

def upper_case(list_names):
    return [name.upper() for name in list_names] 

names = ['adrian','moises','lorena']
print(upper_case(names))

#//////============================================\\\\\\\\\
#//////============================================\\\\\\\\\
#//////============================================\\\\\\\\\

# Crie uma única expressão lambda que:

# Receba a lista employees
# Filtre apenas os funcionários ativos
# Aplique 10% de aumento no salário deles
# Retorne uma nova lista de dicionários
# Ordene o resultado pelo salário crescente
# Não modifique a lista original

employees = [
    {"name": "Ana", "salary": 3000, "active": True},
    {"name": "Carlos", "salary": 2500, "active": False},
    {"name": "Bianca", "salary": 4000, "active": True},
    {"name": "Daniel", "salary": 2000, "active": True},
] 

employe_aument = sorted([{**employe ,'salary':employe['salary'] + (employe['salary'] * (10 / 100))}
                         for employe in employees if employe['active']],
                        key=lambda salary: salary['salary'])

print(*employe_aument,sep='\n')

#//////============================================\\\\\\\\\
#//////============================================\\\\\\\\\
#//////============================================\\\\\\\\\

# Exercício 1:
# Criar uma função usando lambda e closure que retorne outra função.
# A função retornada deve multiplicar um valor por um fator fixo.

multiply = (lambda factor: lambda value: factor* value)
multiply_two = multiply(2)
multiply_three = multiply(3)

print(multiply_two(5))
print(multiply_three(5))

# Exercício 2:
# Criar uma lista com apenas os produtos ativos.
# Aplicar 10% de desconto no preço de cada produto.
# Criar um novo dicionário contendo apenas o nome e o preço final.
# Utilizar list comprehension (sem for tradicional).

products = [
    {"name": "Keyboard", "price": 100, "active": True},
    {"name": "Mouse", "price": 50, "active": False},
    {"name": "Monitor", "price": 900, "active": True},
    {"name": "USB Cable", "price": 30, "active": True},
]

discount = 10 

list_active = [{'name':product['name'] , 'final_price':product['price'] - (product['price'] * (discount / 100))}
for product in products if product['active']]

print(*list_active,sep='\n')

#//////============================================\\\\\\\\\
#//////============================================\\\\\\\\\
#//////============================================\\\\\\\\\

# ==Exercício 1==
# Crie uma função que receba uma lista de nomes
# e retorne um dicionário agrupando os nomes
# pela primeira letra.
user_names = ['adrian','moises','gabriel','andersson','limeira']

def creat_order_name(list_name): 
    dic_order = {}
    for name in list_name:
        first_letter = name[0]
        if first_letter in dic_order:
            dic_order[first_letter].append(name)
        else:
            dic_order[first_letter] =  [name]
    return dic_order

print(creat_order_name(user_names))

# ==Exercício 2==
# Dada uma lista de números,
# crie uma nova lista contendo apenas
# os números pares elevados ao quadrado,
# usando list comprehension.

numbers = [10, 15, 20, 25, 30, 35, 40]

square_number = [number**2 for number in numbers if number % 2 == 0]
print(square_number)


# ==Exercício 3==
# Dada uma lista de palavras,
# ordene usando sorted():
# 1) Pela última letra
# 2) Em caso de empate, pelo tamanho da palavra

words = ["banana", "apple", "kiwi", "grape","bananana"]
mino = len(min(words))
words_order = sorted(words, key=lambda l:(l[-1],len(l)))
print(*words_order,sep='\n')

#//////============================================\\\\\\\\\
#//////============================================\\\\\\\\\

# exercicio 1
# Crie uma função que:
# receba uma lista de palavras
# retorne um dicionário onde:
# a chave é o tamanho da palavra
# o valor é uma lista com palavras daquele tamanho

def size_words(words):
    dic_words = {}
    for word in words:
        size_letter = len(word)
        if size_letter in dic_words:
            dic_words[size_letter].append(word)
        else:
            dic_words[size_letter] = [word]
    return dic_words
words_list = ["python", "java", "c", "ruby", "go"]
print(size_words(words_list))

#//////============================================\\\\\\\\\
#//////============================================\\\\\\\\\
# exercicio 2
# Crie uma função que:
# receba uma frase (string)
# conte quantas vezes cada letra aparece
# ignore espaços
# ignore maiúsculo/minúsculo ("A" == "a")


def count_letter(text):
    dic_count = {}
    for letter in text.replace(" ", "").lower():
        if letter in dic_count:
            continue
        dic_count[letter] = text.count(letter)
    return dic_count

text = "Hello World"
print(count_letter(text))
#//////============================================\\\\\\\\\
#//////============================================\\\\\\\\\
# exercicio 3
# Crie uma função que:
# calcule a média de cada aluno
# retorne uma lista de tuplas:
# ordenada da maior média para menor.

students = {
    "Ana": [8, 7, 9],
    "Carlos": [5, 6, 7],
    "Joao": [10, 9, 8]
}

def mean_student(list_studant):
    return [(key,(sum(value) / len(value))) for key,value in list_studant.items()]

ordered_students = sorted(mean_student(students), key=lambda student:student[1], reverse=True)
print(*ordered_students,sep='\n')



