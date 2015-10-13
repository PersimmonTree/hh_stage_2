import getopt
import sys
import sympy
import re

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
        s = re.sub("([a-z])(\()", lambda m: m.group(1) + " * " + m.group(2), s)
        s = re.sub('(\d)([a-z])', lambda m: m.group(1) + " * " + m.group(2), s)
    return s

def prettify(s):
    s = re.sub("\*\*", "^", s)
    s = re.sub("\*", "", s)
    return s

def usage():
    print("Usage..........")

def main(argv):

    _filePath = None

    try:
        opts, args = getopt.getopt(argv, "h:f:", ["help", "filePath="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit(2)
        elif opt in ("-f", "--filePath"):
            _filePath = arg

    s = argv[0]

    try:
        s = normalize(s)
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
                    line = normalize(line)
                except ValueError as errorMessage:
                    print(errorMessage)
                try:
                    s = sympy.expand(s)
                except SyntaxError:
                    print("Выражение не может быть приведено к стандартному виду.")
                print(prettify(str(s)))

    return 0

if __name__ == '__main__':
    status = main(sys.argv[1:])
    sys.exit(status)