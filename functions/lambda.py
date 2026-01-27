#lambda , pode conter closure tbm



products = [
    {"name": "Keyboard", "price": 100, "tax": 0.10},
    {"name": "Mouse", "price": 50, "tax": 0.05},
    {"name": "Monitor", "price": 800, "tax": 0.15}
]

for item_price in products:
    print('preço antigo', item_price['name'] ,item_price['price'])

    calculate_taxes = (lambda price: lambda tax: price + (price * tax))(item_price["price"])


    item_price['price'] = calculate_taxes(item_price['tax'])

order_price = sorted(products, key=lambda value: value["price"])

for i,item in enumerate(order_price):
    print(i, item)


products = [
    {"name": "Keyboard", "price": 100},
    {"name": "Mouse", "price": 50},
    {"name": "Monitor", "price": 800}
]

def list_product(function,*args):
    return function(*args)
for product in products:
    taxs = list_product(lambda product: lambda tax: product + (product * tax),
    product["price"])
    print(f'{product["name"]} {taxs(10 / 100)} aumento 10%')







a,a1,b,b1,*_ = 1 , 2 , 3 , 4, 5 , 6, 7 , 8
print(a + a1, *_)

pessoa = { 
    'nome':'adrian',
    'sobrenome':'moises'
}
pessoa1 = { 
    'nom1e':'adrian',
    'sobren1ome':'moises'
}

(a,a1),(b,b2) = pessoa.items()

print(a,b2,b,a1)


for key,value in pessoa.items():
    print(key,value)

dic3 = {**pessoa1 , **pessoa}

print(dic3)


def argumentos(*args,**kwargs):
    for key in args:
        print('nao nomeados', key)
    for key,value in kwargs.items():
        print(key,value)
    

argumentos(**dic3)





#lambda
lista = []
def excuta(funcao, *args):
    return funcao(*args)
greeting_function = excuta(lambda greet: lambda name: greet + name ,'Good morning, '  )
taxes = excuta(lambda value_product: lambda tax_value: value_product + (value_product * tax_value),20)
ordem = excuta(lambda *args: lista.append(list(args)),4,5,2,4,5)
lista[0].sort()
print(lista)
print(f'com taxa valor é {taxes(10 / 100)}\n')
print(greeting_function('Adrian'))

def soma(x,y):
    return x + y

def creat_multiplicador(multi):
    def multiplica(numero):
        return multi * numero
    return multiplica
oi = creat_multiplicador(5)
print(excuta(lambda multi,numero: multi * numero, 5,10),

)
duplica = excuta(lambda m: lambda n: n * m ,5)
print(duplica(2))

elogio = excuta(lambda m: lambda n: m + n,'adrian, ')
print(elogio('bunito'))




print(
    excuta(soma, 1 , 2),
    soma(2,3),
    excuta(lambda x , y: x + y, 1,2)

)

exit()




people = [
    {"name": "Carlos", "age": 30},
    {"name": "Ana", "age": 22},
    {"name": "Bruno", "age": 25},
    {"name": "Daniela", "age": 28}
]

def orden_age(list_age):
    for age in list_age:
        print(age)

age_old = sorted(people, key=lambda old: old["age"])

orden_age(age_old)

for name in people:
    print(name)



exit()
students = [
    {"name": "Lucas", "grade": 8.0},
    {"name": "Ana", "grade": 9.5},
    {"name": "Pedro", "grade": 8.0},
    {"name": "Marina", "grade": 7.5}
]

def exibir(list_):
    for studants_grades in list_:
        print(studants_grades)





grade = sorted(students,key=lambda studant: (studant["grade"], studant["name"]))


exibir(grade)




exit()
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





l1 = sorted(lista, key=lambda name: name['nome'])
l2 = sorted(lista, key=lambda name: name['sobrenome'])

exibir(l1)
exibir(l2)



lista = [{'ID': 0, 'Name': 'mause', 'price': 38.5, 'tax': 10.0},{'ID': 0, 'Name': 'mause', 'price': 33.5, 'tax': 10.0},{'ID': 0, 'Name': 'mause', 'price': 34.5, 'tax': 10.0}]

def executa(fuction,*args):
    return fuction(*args)
for item in lista:
    tax_product = executa(lambda price: lambda tax: price + (tax * price) , item['price'])
    print(tax_product(item['tax'] / 100))
greeting = executa(lambda greet: lambda name: greet + name,'Good morning, ')
print(greeting('Adrian'))
