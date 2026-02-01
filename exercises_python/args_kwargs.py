#somando valores
def sum_values(*values):
    final_value = 0
    for value in values:
        final_value += value
    return final_value

print(sum_values(1,2,3,4,5))

# usando comprehension
def sum_values(*values):
    value_final = 0
    return sum([value for value in values])
print(sum_values(1,2,3,4,5))

#mostrando user
def show_data(**user_data):
    return user_data
    
print(show_data(name='Adrian',age='18'))