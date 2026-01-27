#set em pytthon 

exit()
def duplicado_number(lista_inteiros):
    s1 = set()
    for i,numero in enumerate(lista_inteiros):
        if numero in s1:
            return numero , i
        s1.add(numero) 
    return -1
    

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

for lista in lista_de_listas_de_inteiros:
    print(f'{lista} {duplicado_number(lista)}')



def duplicado_number(lista_inteiros):
    s1 = set()
    cont = 0
    for numero in lista_inteiros:
        if numero in s1 and cont < 1:
            cont += 1
            return numero
        s1.add(numero)
    return -1
            
    

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

for lista in lista_de_listas_de_inteiros:
    print(duplicado_number(lista))




exit()

def creat_set():
    s1_ = set()
    def add_value(value):
        s1_.add(value)
        return s1_
    return add_value

value_set = creat_set()

print(value_set(4))
print(value_set(3))
print(value_set(3))




def create_intersection(s1):
    def intersection(s2):
        return s1 & s2
    return intersection



set_1 = create_intersection({1,2,3,4,5})
print(set_1({2,}))



def block_user():
    s1 = set()

    def block(user):
        s1.add(user)
        return s1
    return block


block = block_user()
list_user = ['adrian','adrian','lorena','adrian','adrian','lorena']
for name in list_user:
    
    print(block(name))


li = [1,2,3,3,3,3,3,1,2]
sets = list(set(li))
print(sets)
s1 = set()
for value in li:
    s1.add(value)
    if value in [1,2]:
        s1.discard(value)
print(s1)
s2

s3 = s1 & s2
s3 = s1 | s2
s3 = s2 - s1
print(s3)

