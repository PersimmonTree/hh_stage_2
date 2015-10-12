# 1. Полином
# Дано выражение, содержащее скобки, операции сложения, вычитания, умножения, возведения в константную степень
# и одну переменную, например: (x - 5)(2x^3 + x(x^2 - 9)).

# Представьте это выражение в развёрнутом виде, например: 3x^4 - 15x^3 - 9x^2 + 45x

import sys
import sympy
import re

s = "(a - 5)(2a^3 + a(a^2 - 9))"

def normalizer(s):

    def varCounter(s):
        vars = []
        for c in s:
            if c.isalpha() and c not in vars:
                vars.append(c)
        return len(vars)

    s_varNum = varCounter(s)

    if s_varNum == 0:
        raise ValueError('Выражение не содержит ни одной переменной.')
    elif s_varNum > 1:
        raise ValueError('Выражение содержит больше одной переменной (примечание: Программа чувствительна к регистру.)')
    elif s_varNum == 1:
        s.lower()
        s = re.sub("\)\(", ") * (", s)
        s = re.sub("\^", " ** ", s)
        s = re.sub("([a-z])(\()", lambda m: m.group(1) + " * " + m.group(2), s)
        s = re.sub('(\d)([a-z])', lambda m: m.group(1) + " * " + m.group(2), s)
    return s

def main(args = None):

    s = input("Введите выражение, которое требуется привести к стандартному виду: ")

    try:
        s = normalizer(s)
    except ValueError as errorMessage:
        print(errorMessage)
        return -1

    try:
        s = sympy.expand(s)
    except SyntaxError:
        print("Выражение не может быть приведено к стандартному виду.")
        return -1

    print(s)
    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)

# s = normalizer(s)
# print(sympy.expand(s))