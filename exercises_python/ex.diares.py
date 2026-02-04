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

# Exercício:
# Criar uma função usando lambda e closure que retorne outra função.
# A função retornada deve multiplicar um valor por um fator fixo.

multiply = (lambda factor: lambda value: factor* value)
multiply_two = multiply(2)
multiply_three = multiply(3)

print(multiply_two(5))
print(multiply_three(5))

# Exercício:
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