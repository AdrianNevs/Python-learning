# dicionarios com comprehension_filter
import pprint

def p(valor):
    return pprint.pprint(valor)
# uso do comprehension com str
linha = []
lista = [ [ letra for letra in 'luiz']
          for x in range(3) 
         ]

p(lista)


# adicionando tax em produtos
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

#gera uma nova lista e aplica apenas taxa nos preços < 20  e lita apenas produtos < 20
tax_aument = [{**products, 'preco':products['preco'] * 1.5}
              if products['preco'] < 20 else products
               for products in produtos if products['preco'] < 20]

p(tax_aument)




# exercicios para o aprendizado
products = [
    {'name': 'Keyboard', 'price': 100},
    {'name': 'Mouse', 'price': 50},
    {'name': 'Monitor', 'price': 800},
    {'name': 'USB Cable', 'price': 20},
]
# verifica e lista apenas preços menores < 25
verifiction_price = [produto for produto in produtos 
                    if produto['preco'] < 25]
# gera uma nova lista e aplica a taxa nos produtos com uma copia rasa
create_tax = [{**produto, 'preco':produto['preco'] * 0.10 + produto['preco']}
                    for produto in produtos]
# gera uma nova lista e aplica a taxa nos produtos e lista apenas produtos >= 20
verific_price_tax = [{**produto, 'preco':produto['preco'] * 0.05 + produto['preco']}
                    for produto in produtos if produto['preco'] >= 20]
#gera uma nova lista e aplica a taxa nos produtos e lista todos produtos e aplica
#taxa apenas nos preços > 20
price_verific = [{**produto, 'preco':produto['preco'] * 0.05 + produto['preco']}
                  if produto['preco'] > 20 else produto
                  for produto in produtos]
#gera uma nova lista e aplica apenas taxa nos preços > 100  e lita apenas produtos >=50
#

list_price = [{**product, 'price':product['price'] - (product['price'] * 0.10)}
              if product['price'] > 100 else product
              for product in products if product['price'] >= 50]

p(verifiction_price)
p(create_tax)
p(verific_price_tax)
p(price_verific)
p(list_price)
