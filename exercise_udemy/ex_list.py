# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
city_list = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado_list = ['BA', 'SP','MG','RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(citys): #usando closure
    def unir(estado):
        new_list = []
        for i,city in enumerate(citys):
            if i >= len(estado):
                break
            new_list.append((city,estado[i]))
        return new_list
    return unir

unir_city_estado = zipper(city_list)
print(unir_city_estado(estado_list))

#/////////=====================================\\\\\\\\\
#exemplo usando decorador 
def decorador(func):
    def interno(*values,**kwargs):
        print('passei aqui')
        result =  func(*values,**kwargs)
        return result 'modificando'
    return interno

@decorador
def zipper(cities,estado):
    new_list = []
    for i,city in enumerate(cities):
        if i >= len(estado):
            break
        new_list.append((city,estado[i]))
    return new_list


unir_city_estado = zipper(city_list,estado_list)
print(*unir_city_estado)

#/////////=====================================\\\\\\\\\
#maneira mais simples
#uso de if ternario e list comprehension
def zipper(city_l1, estado_l2):
    size_list = len(city_l1) if len(city_l1) < len(estado_l2) else len(estado_l2) # ou size_list = min(len(city_l1),len(estado_l2))
    return  [(city_l1[i],estado_l2[i]) for i in range(size_list)]
print(zipper(city_list,estado_list))
