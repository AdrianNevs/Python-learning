# aprendendo sobre decoradores em python
# com o uso do @

def is_int_float(param): #verificar se contem str
    if not isinstance(param,(int,float)):
        raise ValueError('Passou uma str')

def with_user_name(name=None): #recebe um nome, se nao receber valor None
    def create_decorador(func): #criando decorador , vai retornar nome é a tax calculada
        def interno(*args,**kwargs):
            print(f'Seu nome é {name}')
            for param in args:
                is_int_float(param)
            result = func(*args,**kwargs)
            return result,f'{name}'
        return interno
    return create_decorador

@with_user_name(name='Adrian')
def tax_value(value,tax): #calcular taxa de forma simples e facil
    return value + ((tax / 100) * value)

tax_calculate = tax_value(400,10)
print(tax_calculate)

#///////////////=====================================================\\\\\\\\\\\\\\\\\\\\\\\
#decorador soma
#funcao de somar valores usando decorador 
def valid_value(param): #funcao para validar se nao contem str
    if not isinstance(param,(int,float)):
        raise ValueError('Passou uma str')
    
def create_function(function):
    def interna(*args,**kwargs):
        for param in args: 
            valid_value(param)
        result = function(*args,**kwargs)
        return result
    return interna

@create_function
def sum_values(x,y): # funcao soma ligada ao decorador
    return x + y

tax_calculate_1 = create_function(lambda value: lambda tax: value + ((tax/ 100) * value))(400) # closure em lambda, usando decorador
print(tax_calculate_1(2)) # aqui nao valida o uso do decorador 

tax_calculate = create_function(lambda value, tax: value + ((tax/ 100) * value))(400,10) # com uma lambda, usando decorador
print(tax_calculate)

sum_value_10 = sum_values(10,12)
print(sum_value_10)

#///////////////=====================================================\\\\\\\\\\\\\\\\\\\\\\\
#///////////////=====================================================\\\\\\\\\\\\\\\\\\\\\\\
# Decorator que valida se todos os argumentos posicionais são strings.
# Lança TypeError caso um valor inválido seja passado.
# Aplicação manual do decorator (sem uso do @)
def creat_funcion(func): #decorador
    def interno(*args,**kwargs):
        for param in args:
            is_str(param)
        result = func(*args,**kwargs)
        return result
    return interno

def reverse_str(msg):
    return msg[::-1]

def is_str(param):
    if not isinstance(param,(str)):
        raise TypeError('voce passou um valor int')

inverter = creat_funcion(reverse_str)
print(inverter('123'))

# Exercício 1: decorator que valida parâmetros do tipo string,
# retorna a string em uppercase e invertida, lançando TypeError em caso de erro
# Aplicação manual do decorator (sem uso do @)
def validate_string_params(function):
    def interno(*args,**kwargs):
        for param in args:
            if not isinstance(param,str):
                raise TypeError('Passou um int')
        resultado = function(*args,**kwargs)
        return resultado
    return interno
            

def reverse_string(text):
    return text[::-1]

def upper_str(text):
    return text.upper()

reverse_text = validate_string_params(reverse_string)
print(reverse_text('adr'))
upper_text = validate_string_params(upper_str)
print(upper_text('adrian'))
