# raise em python
def error_dividir_zero(x , y):
    
    if isinstance (x,str) or isinstance(y,str):
        raise TypeError('str caceta nao e int') #cria proprio erro e renomeia
    else:
        if x  == 0 or y == 0:
            raise ZeroDivisionError('nao se divide 0')
        
error_dividir_zero(10 , 0)
