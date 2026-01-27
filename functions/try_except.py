lista = []

try:
    x = 10
    y = 0
    print('texto' + x)
    division = x / y
    #z = 12
    #sum(x,z)
    print('valor'[1000])
except (ZeroDivisionError , NameError) as error:
    print('ocorreu erro')
    print(error.__class__.__name__) # mostrar seu repesctivo nome do erro .class.name
except (IndexError,TypeError) as error:
    print('erro e seu nome')
    print(error.__class__.__name__)
except Exception as error:
    print('erro desconhecido')
    print(error.__class__.__name__)
else:
    print('nao ocorreu erros') # quando nao haver erros
finally: 
    print('roda mesmo que ocorra erro') # sempre executa
    print('sempre vai executar')


#exercicio

while True:
    #menu
    print('==Selecione uma opcão==')
    Peso = str(input('[i]nserir [a]pagar [l]istar [S]air')).lower()
    #validar opcoes
    if 'i' == Peso:
        lista.append(input('Valor: '))
    elif 'a' == Peso:
        if len(lista) == 0:
            print('lista vazia')
        else:
            try:
                Peso = int(input('escolha o indice: '))
                del lista[Peso]
            except IndexError:
                print('indice invalido')
            except ValueError:
                print('Digite um numero inteiro')
            except Exception:
                print('Erro desconhecido')
    elif 'l' == Peso:
        
        if len(lista) == 0:
            print(f'\n==nada para listar==\n')
        else:
            for i in range(len(lista)):
                print(i, lista[i])
    elif 's' == Peso:
        break
    else:
        print('Digite apenas [i,a,l,s]')
