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
