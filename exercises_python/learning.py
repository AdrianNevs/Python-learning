# EX1: Encontrar o segundo maior número de uma lista
# O algoritmo encontra o maior valor da lista, remove todas as ocorrências
# desse valor e depois executa novamente a função para encontrar o próximo maior,
# que será o segundo maior número.
# Use função recursiva

numbers = [5, 9, 9, 1, 5, 9]

def two_size(list_numbers, c=0):
    copy_list = list_numbers.copy()

    one_value = list_numbers[0]

    for value in list_numbers:
        if one_value < value:
            one_value = value

    if c == 1:
        return 'segundo maior valor', one_value
    else:
        while one_value in copy_list:
            copy_list.remove(one_value)
        c = 1
        return two_size(copy_list, c)

print(two_size(numbers))


# EX2: Filtrar produtos por faixa de preço
# A função recebe um dicionário de produtos com seus preços
# e permite filtrar pelos seguintes casos:
# - apenas preço mínimo
# - apenas preço máximo
# - preço mínimo e máximo
# O resultado é retornado ordenado pelo preço.

products = {
    "notebook": 3500,
    "mouse": 80,
    "keyboard": 200,
    "monitor": 900,
    "usb_cable": 25,
    "webcam": 150
}

def filter_products(products, min_price=None, max_price=None):
    if max_price is None and min_price is None:
        return 'Adicione valor max e min'
    
    elif min_price is None or max_price is None:
        result = [(key,value) for key,value in products.items() if value >= min_price] if max_price is None and min_price is not None else [(key,value) for key,value in products.items() if value <= max_price]

        return sorted(result,key=lambda n:n[1])
    
    result = [(key,value) for key,value in products.items() if value >= min_price and value <= max_price]
    return sorted(result,key=lambda n:n[1])

print(filter_products(products,10))


# EX3: Filtrar preços dentro de um dicionário
# A função recebe um dicionário contendo preços e retorna
# apenas os valores que estão dentro de uma faixa definida.
# A função funciona nos seguintes casos:
# - apenas valor mínimo
# - apenas valor máximo
# - valor mínimo e máximo

def filter_prices(price_dict, min_price=None, max_price=None):

    if min_price is None and max_price is None:
        return 'Adicione valor mínimo e máximo'

    elif min_price is None and max_price is not None:
        return [price for price in price_dict.values() if price <= max_price]

    elif max_price is None and min_price is not None:
        return [price for price in price_dict.values() if price >= min_price]

    return [price for price in price_dict.values() if min_price <= price <= max_price]


price_dic = {'price':110, 'p2':200 , 'p3':30}

print(filter_prices(price_dic, max_price=10))
