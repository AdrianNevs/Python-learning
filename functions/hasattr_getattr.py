# aprendizado com hasattr e getattr

#sem if ternario
str1 = 'luz'
method_test = 'upper1'
def apply_method(value,method):
    if hasattr(value,method):
        return getattr(value,method)()
    
    return f'method no found {method}'


value_user = input('Digite oque deseja aplicar')
method_user = input('Digite metado deseja aplicar').lower()

print(apply_method(str1,method_test))
print(apply_method(value_user,method_user))

#com if ternario 


str1 = 'luz'
method_test = 'upper1'
def apply_method(value,method):
    return getattr(value,method)() if hasattr(value,method) else f'method no found {method}'



value_user = input('Digite oque deseja aplicar')
method_user = input('Digite metado deseja aplicar').lower()

print(apply_method(str1,method_test))
print(apply_method(value_user,method_user))

#com closure

value = 'luz'
method = 'upper1'

def apply_value(value):
    def apply_method(method):
        if hasattr(value,method):
            return getattr(value,method)()
        else:
            return f'method no found, {method}'
    return apply_method

creat_method = apply_value(value)
print(creat_method(method))
