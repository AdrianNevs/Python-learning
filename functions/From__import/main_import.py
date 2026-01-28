from import_past.learning_import import closure_tax
import import_past
from sys import path

# __init__
greet = import_past.greeting('Good Morning')
print(greet('adrian'))
#acesso a variaveis e def que importei no __init__
print(import_past.v)

# learning_import
value = closure_tax(5)
print(value(10))


# ver local dos arquivos
# for local in path: 
#     print(local)


