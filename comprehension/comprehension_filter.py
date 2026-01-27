# dicionarios com comprehension_filter
import pprint

def p(valor):
    return pprint.pprint(valor)

linha = []
lista = [ [ letra for letra in 'luiz']
          for x in range(3) 
         ]

p(lista)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]


tax_aument = [{**products, 'preco':products['preco'] * 1.5}
              if products['preco'] < 20 else products
               for products in produtos if products['preco'] < 20]

p(tax_aument)





products = [
    {'name': 'Keyboard', 'price': 100},
    {'name': 'Mouse', 'price': 50},
    {'name': 'Monitor', 'price': 800},
    {'name': 'USB Cable', 'price': 20},
]

verifiction_price = [produto for produto in produtos 
                    if produto['preco'] < 25]

create_tax = [{**produto, 'preco':produto['preco'] * 0.10 + produto['preco']}
                    for produto in produtos]

verific_price_tax = [{**produto, 'preco':produto['preco'] * 0.05 + produto['preco']}
                    for produto in produtos if produto['preco'] >= 20]

price_verific = [{**produto, 'preco':produto['preco'] * 0.05 + produto['preco']}
                  if produto['preco'] > 20 else produto
                  for produto in produtos]
# 5 final

list_price = [{**product, 'price':product['price'] - (product['price'] * 0.10)}
              if product['price'] > 100 else product
              for product in products if product['price'] >= 50]

p(verifiction_price)
p(create_tax)
p(verific_price_tax)
p(price_verific)
p(list_price)
