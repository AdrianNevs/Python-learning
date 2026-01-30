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
