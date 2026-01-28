v = 'oi'
def closure_tax(value):
    def calculate_tax(tax):
        return value + (value * (tax / 100))
    return calculate_tax