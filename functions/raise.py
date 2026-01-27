# aprendendo uso do raise

# exercicio 1
def safe_multiply(a,b):
    if isinstance (a,str) or isinstance(b,str):
        raise type('apenas numero nao str')
    else:
        return a * b

print(safe_multiply(2,'value'))
# exercicio 2

def convertion_int(value):
    if isinstance(value,(int,float)):
        return int(value)
    raise ValueError('apenas int or float')

print(convertion_int('oi'))

#exercicio 3

def error_dividir_zero(x , y):
    if isinstance (x,str) or isinstance(y,str):
        raise TypeError('str não divide') # Erro personalizado
    else:
        if y == 0:
            raise ZeroDivisionError('nao se divide 0')
    return x / y
        
print(error_dividir_zero(10 , 0))

#exercicio 4

def calculate_division(a,b):
    try:
        if isinstance(a,str) or isinstance(b,str):
            raise TypeError('nao multiplica strings')
        if b == 0: 
            raise ZeroDivisionError('tentou dividir por 0')
        division = a / b
        print(division)
        return division
    except Exception as error:
        print(error)
        print(f'{error.__class__.__name__}\n')

value = [(10,2), (0,5), (8,0), ("3",3)]

for item in value:
    calculate_division(item[0],item[1])
