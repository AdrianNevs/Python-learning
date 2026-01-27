# from yield

def gen1():
    yield 1
    yield 2
    yield 3

def gen2(gen=None):
    if gen is not None: 
        yield from gen()
    yield from (n for n in range(4,20) if n % 2 == 0)

gen_uniao = gen2(gen1)
for number in gen_uniao:
    print(number)
