#tenho acesso todos 
# variaveis e def que escolher
from import_past.learning_import import closure_tax,v # usar * teria acesso a todas variaveis e def do arquivo.py

# inicia quando é exportado a pasta
print('Você importou',__name__)

#pode criar funcoes caso queira, sem precisar usar o from para exportar.
def greeting(greet):
    def name_user(name):
        return greet,name
    return name_user