import math


lam1 = lambda a: a**2
lam2 = lambda b,c: math.sqrt(b**2 + c**2)
lam3 = lambda *args: sum(args) /len(args)
lam4 = lambda d: "".join(set(d))

def ffn(a):
    return a**2

def sfn(b, c):
    return math.sqrt(b**2 + c**2)

def tfn(*args):
    return sum(args) /len(args)

def ftfn(d):
    return ''.join(set(d))

print(ffn(7))
print(sfn(7, 7))
print(tfn(1, 2, 3, 4))
print(ftfn('work'))