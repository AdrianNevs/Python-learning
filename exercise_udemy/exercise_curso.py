#sistema de questoes em py

import os
def system_question(valor):
    cont = 0
    for p in question:
        print(p['Pergunta'])
        for i,opcoes in enumerate(p['Opções']):
            print(f'{i})',opcoes)
        while True:
            user_1 = (input('Digite:'))
            if user_1.isdigit():
                user_1 = int(user_1)
            else:
                print('apenas numeros')
                continue
            if user_1 <= len(p['Opções']) - 1 and user_1 >= 0:
                break
            
        if int(p['Resposta']) == int(p['Opções'][user_1]):
            os.system('cls')
            cont += 1
            print('Acertou!')
        else:
            os.system('cls')
            print('errou')
    return f'acertou {cont}'
    

question = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51','56'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
system_question(question)
for pergunta in question:
    
    print(f'pergunta: {pergunta['Pergunta']}\n')
    for i,opcao in enumerate (pergunta['Opções']):
        print(f'{i}) {opcao}')
    print()
    usuario = input('digite:')

    acertou = False
    respostas = pergunta['Resposta']
    size_question = len(pergunta['Opções'])
    validar_digito = int(usuario) if usuario.isdigit() else None
    if validar_digito is not None:
        if validar_digito >= 0 and validar_digito < size_question:
            if pergunta['Opções'][validar_digito] == respostas:
                acertou = True
            else:
                acertou = False

    if acertou:
        acertos += 1
        print('Acertou!')
    else:
        print('Errou!')
print(f'voçê acertou {acertos}')




exit()
def system_question(valor):
    for i in range(len(question)):
        print(question[i]['Pergunta'])
        for j in range(len(question[i]['Opções'])):
            print(f'{j})',question[i]['Opções'][j])
        while True:
            try:
                user_1 = int(input('Digite:'))
                if user_1 <= len(question[i]['Opções']) - 1 :
                    break
                else:
                    print('não existe esse indice')
                    continue
            except ValueError:
                print('apenas numeros')
        if int(question[i]['Resposta']) == int(question[i]['Opções'][user_1]):
            os.system('cls')
            print('Acertou!')
        else:
            os.system('cls')
            print('errou')
    

question = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51','56'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
system_question(question)
