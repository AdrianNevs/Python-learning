
#Exercício 1 — Soma Recursiva (fundamental)
# Crie uma função recursiva que calcule:
# 1 + 2 + 3 + ... + N: 

def sum_recursive(n):
    if n <= 0:
        return 0 
    return n + (sum_recursive(n - 1))
print(sum_recursive(10))


# Exercício 2 — Filtrar números (nível clean code)

# Crie uma função que:
# remove números negativos
# ignora zeros
# retorna apenas números pares multiplicados por 2
# usando def 

list_number = [10, -1, 10, 0, -7, 8, 5]
def mult(list_number):
    new_list = []
    for n in list_number:
        if n <= 0:
            continue
        if n % 2 != 0:
            continue
        new_list.append(n * 2)
    return new_list

print(mult(list_number))

#usando def e comprehesion
def mult(list_number):
    return [n * 2 for n in list_number 
            if n > 0 and n % 2 == 0]

print(mult(list_number))

#usando lambda
mult1 = (lambda list_n:[n * 2 for n in list_n
            if n > 0 and n % 2 == 0])(list_number)
print(mult1)

# 🥉 Exercício 3 — Fatorial sem acumulador (LEVEL UP)
# Agora faça o fatorial:
# factorial(5) → 120
# Mas:
# sem variável acumuladora
# sem segundo parâmetro

def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n - 1)
print(factorial(5))


# Exercicio 4 final:
# A função deve:
# Percorrer a lista sem utilizar estruturas de repetição (for ou while);
# Utilizar recursão para avançar elemento por elemento;
# Usar parâmetros auxiliares para:
# controlar o índice atual da lista;
# acumular a quantidade de números pares encontrados;
# Retornar ao final da execução a quantidade total de números pares presentes na lista.
# 📌 Requisitos
# Não criar novas listas durante o processo;
# Não usar funções prontas como filter() ou sum();
# A solução deve ser totalmente recursiva.

def recursive_par(l,c,p):
    if len(l) <= c:
        return p
    if l[c] % 2 == 0:
        p += 1
    c += 1
    return recursive_par(l,c,p)
print(recursive_par(list_number,0,0))
