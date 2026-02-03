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

def zipper(citys):
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
