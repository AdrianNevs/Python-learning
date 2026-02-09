# aprendendo utilizacao do map
# calcular taxas da lista
list_price = [100,200,300,400]
def add_taxes(value):
    if value <= 200:
        return value * 1.1
    return value * 2.2

print(list(map(add_taxes,list_price)))
#usando lambda,map para calcular taxa 
taxes = list(map(lambda value:value * 1.2 if value >= 200 else value * 1.1,list_price))
print(*taxes,sep='\n')

#def que adiciona * a cada frase
#utilizando map para passar em cada item da lista
list_phrase = ['adicionando','varios','pontinhos']
def add_point(msg):
    return f'{msg}*'

new_phrase = list(map(add_point,list_phrase))
print(*new_phrase)
#utilizando lambda e map,para gerar uma nova frase com pontos
new_phrase = list(map(lambda msg: f'{msg}*',list_phrase))
print(*new_phrase)



# def saudar utiliza uma lista de nomes
# retorna uma lista com todos nomes com as saudações
# usando sep='\n' para separar cada saudação
list_name = ['adrian','moises','josé']
def greeting(msg):
    return f'{msg} Good morning'

greeting_list = list(map(greeting,list_name))
print(*greeting_list,sep='\n')
#utilizando lambda + map
greeting_list = list(map(lambda n: f"{n} good morning",list_name))
print(*greeting_list,sep='\n')

