# aprendendo sombre itertools  
# exercicios feitos sem funcao pronta, para aprender logica de programação
# aprendendo a utilizar a biblioteca itertools 
from itertools import combinations, permutations, product, groupby
pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisa = ['azul','branco']

# combinacao sem repeticao 
new_list = []
for i in range(len(pessoas)):
    for j in range(i + 1, len(pessoas)):
        new_list.append((pessoas[i], pessoas[j]))

print(new_list)

new_list = []
#sem funcao pronta entendendo como funciona a logica
#totas combinacoes possiveis sem repetir o mesmo nomes
for i in range(len(pessoas)):
    for j in range(0 ,len(pessoas)):
        if i != j:
            new_list.append((pessoas[i],pessoas[j]))
print(new_list)

#usando comprehension entendendo a logica
pares_invertidos = [
    (pessoas[i],pessoas[j])
     for i in range(len(pessoas))
     for j in range(len(pessoas))
     if i != j]
print(*pares_invertidos,sep='\n')

#maneira simples
print(list(combinations(pessoas,2))) #lista com cobinacao sem repeticao
#==================/////////////\\\\\\\\\\\\=============================
print(list(permutations(pessoas,2))) #lista com todas combinacoes
# combinacao de duas listas 
print(list(product(pessoas,camisa)))

#==================/////////////\\\\\\\\\\\\=============================
#==================/////////////\\\\\\\\\\\\=============================


student_list = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},]

def order_list(student):
    return student['nota']

order_student = sorted(student_list,key=order_list) # ordernar a lista por nota
groups = groupby(order_student, key=order_list)

for key,group in groups:
    print(key) 
    for student in group:
        print(student)
