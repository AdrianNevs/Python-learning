# exercicio copy, sorted, produtos.sort
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# meu codigo resolvendo o exercicio
import copy

tax_list = [{**produto ,'preco':produto['preco'] * (10 / 100) + produto['preco'],} for produto in copy.deepcopy(produtos)] # Aumente os preços dos produtos a seguir em 10%
                                                                                                                            # Gere novos_produtos por deep copy (cópia profunda)
ordem_decrescente = (sorted(copy.deepcopy(produtos), key=lambda name: name["nome"],reverse=True))      # Ordene os produtos por nome decrescente (do maior para menor)
ordem_crescente = (sorted(copy.deepcopy(produtos), key=lambda name: name["nome"]))       # Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
tax_list_crescente = (sorted(copy.deepcopy(tax_list), key=lambda value: value["preco"]))     # Ordene os produtos por preco crescente (do menor para maior)
tax_list_decrescente = (sorted(copy.deepcopy(tax_list), key=lambda value: value["preco"],reverse=True))    # Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

list_variables = [ordem_decrescente,ordem_crescente,tax_list_crescente,tax_list_decrescente]

for variables in list_variables:
    print(*variables,sep='\n')
    print()
