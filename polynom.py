#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""
Данная программа приводит алгебраическое выражение к стандартному виду.
Допускается ввод выражения из командной строки и из файла (построчно).

Примеры использования:
    >> python3 polynom.py -e "(x-1)(x^2 - 2)*(x ** 4 + 3x + 2)"
    >> python3 polynom.py --filePath "test.txt"
    >> python3 polynom.py --help
"""

import sys
import getopt
import re
import sympy

def normalize(s):

    def varCounter(s):
        vars = []
        for c in s:
            if c.isalpha() and c not in vars:
                vars.append(c)
        return len(vars)

    varNum = varCounter(s)

    if varNum == 0:
        raise ValueError('Выражение не содержит ни одной переменной.')
    elif varNum > 1:
        raise ValueError('Выражение содержит больше одной переменной (примечание: Программа чувствительна к регистру.)')
    elif varNum == 1:
        s.lower()
        s = re.sub("\)\(", ") * (", s)
        s = re.sub("\^", " ** ", s)
        s = re.sub("([a-z0-9])(\()", lambda m: m.group(1) + " * " + m.group(2), s)
        s = re.sub('(\d)([a-z])', lambda m: m.group(1) + " * " + m.group(2), s)
    return s

def prettify(s):
    s = re.sub("\*\*", "^", s)
    s = re.sub("\*", "", s)
    return s

def usage():
    print("Usage: polynom.py"
          "[-h, --help]"
          "[-e string=value, --expression string=value]"
          "[-f path=value, --filePath path=value]")

def main(argv):

    _expression = None
    _filePath = None

    try:
        opts, args = getopt.getopt(argv, "he:f:", ["help", "expression=" ,"filePath="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(2)
        elif opt in ("-e", "--expression"):
            _expression = arg
        elif opt in ("-f", "--filePath"):
            _filePath = arg

    if _expression:
        try:
            s = normalize(_expression)
        except ValueError as errorMessage:
            print(errorMessage)
            return -1

        try:
            s = sympy.expand(s)
        except SyntaxError:
            print("Выражение не может быть приведено к стандартному виду.")
            return -2

        print(prettify(str(s)))

    if _filePath:
        with open(_filePath, 'r') as file:
            for line in file:
                try:
                    s = normalize(line)
                except ValueError as errorMessage:
                    print(errorMessage)
                else:
                    try:
                        s = sympy.expand(s)
                    except SyntaxError:
                        print("Выражение не может быть приведено к стандартному виду.")
                    else:
                        print(prettify(str(s)))

    return 0

if __name__ == '__main__':
    status = main(sys.argv[1:])
    sys.exit(status)