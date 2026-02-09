# aprendendo utilizacao do map
# calcular taxas da lista
list_price = [100,200,300,400]
def add_taxes(value):
    if value >= 200:
        new_price = value * 1.1
    else:
        new_price = value * 2.2
    return new_price

print(list(map(add_taxes,list_price)))

#def que adiciona * a cada frase
#utilizando map para passar em cada item da lista
list_phrase = ['adicionando','varios','pontinhos']
def add_msg(msg):
    new_msg = f'{msg}*'
    return new_msg

new_phrase = list(map(add_msg,list_phrase))
print(*new_phrase)

# def saudar utiliza uma lista de nomes
# retorna uma lista com todos nomes com as saudações
# usando sep='\n' para separar cada saudação
list_name = ['adrian','moises','josé']
def greeting(msg):
    new_msg = f'{msg} Good morning'
    return new_msg

greeting_list = list(map(greeting,list_name))
print(*greeting_list,sep='\n')

