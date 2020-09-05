from itertools import product, islice

def expr(p):
    return "{}1{}2{}3{}4{}5{}6{}7{}8{}9".format(*p)

def gen_expr():
    op = ['+', '-', '']
    print([expr(p) for p in product(op, repeat=9) if p[0] != '+'])
    return [expr(p) for p in product(op, repeat=9) if p[0] != '+']

def all_exprs():
    values = {}
    for expr in gen_expr():
        val = eval(expr)
        if val not in values:
            values[val] = 1
        else:
            values[val] += 1
    return values

def sum_to(val):
    for s in filter(lambda x: x[0] == val, map(lambda x: (eval(x), x), gen_expr())):
        print(s)

sum_to(100)
