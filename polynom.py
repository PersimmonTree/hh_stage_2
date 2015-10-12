# 1. Полином
# Дано выражение, содержащее скобки, операции сложения, вычитания, умножения, возведения в константную степень
# и одну переменную, например: (x - 5)(2x^3 + x(x^2 - 9)).

# Представьте это выражение в развёрнутом виде, например: 3x^4 - 15x^3 - 9x^2 + 45x

import sympy
import re

s = "(a - 5)(2a^3 + a(a^2 - 9))"

def varCounter(s):
    vars = []
    for c in s:
        if c.isalpha() and c not in vars:
            vars.append(c)
    return len(vars)

def normalizer(s):
    if varCounter(s) != 1:
        raise Exception("Больше одной переменной в выражении")
    s.lower()
    s = re.sub("\)\(", ") * (", s)
    s = re.sub("\^", " ** ", s)
    s = re.sub("([a-z])(\()", lambda m: m.group(1) + " * " + m.group(2), s)
    s = re.sub('(\d)([a-z])', lambda m: m.group(1) + " * " + m.group(2), s)
    return s

# s = normalizer(s)
# print(sympy.expand(s))