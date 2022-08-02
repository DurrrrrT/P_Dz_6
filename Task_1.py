# Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный.
from re import T


cur_idx = 0


def is_bracket_valid(expr: str):
    parity = 0
    for char in expr:
        if char == '(':
            parity += 1
        elif char == ')':
            parity -= 1
        else:
            pass
        if parity < 0:
            return False
    return parity == 0


def skip_whitespaces(expr: str):
    global cur_idx
    while cur_idx < len(expr) and expr[cur_idx].isspace():
        cur_idx += 1


def get_number(expr: str):
    global cur_idx
    is_int = True
    num_idx = cur_idx

    while cur_idx < len(expr) and expr[cur_idx].isdigit():
        cur_idx += 1
    if cur_idx < len(expr) and expr[cur_idx] == '.':
        is_int = False
        cur_idx += 1
    while cur_idx < len(expr) and expr[cur_idx].isdigit():
        cur_idx += 1
    return int(expr[num_idx:cur_idx]) if is_int else float(expr[num_idx:cur_idx])


def get_term_3(expr: str):
    global cur_idx
    skip_whitespaces(expr)

    if cur_idx > len(expr) - 1:
        return

    if expr[cur_idx] == "(":
        cur_idx += 1
        exp = get_expr(expr)
        skip_whitespaces(expr)
        if expr[cur_idx] == ")":
            cur_idx += 1
            return exp
        else:
            print("Не парные скобки ")
            return
    return get_number(expr)


def get_term2(expr: str):
    global cur_idx
    skip_whitespaces(expr)

    if expr[cur_idx] == '-':
        cur_idx += 1
        return - get_term_3(expr)
    return get_term_3(expr)


def get_term_1(expr: str):
    global cur_idx
    skip_whitespaces(expr)

    term_2 = get_term2(expr)
    if cur_idx > len(expr) - 1:
        return term_2

    skip_whitespaces(expr)
    if expr[cur_idx] == "*":
        cur_idx += 1
        return term_2 * get_term_1(expr)
    elif expr[cur_idx] == "/":
        cur_idx += 1
        return term_2 / get_term_1(expr)

    return term_2


def get_expr(expr: str):
    global cur_idx
    skip_whitespaces(expr)

    term_1 = get_term_1(expr)
    if cur_idx > len(expr) - 1:
        return term_1

    skip_whitespaces(expr)

    if expr[cur_idx] == "+":
        cur_idx += 1
        return term_1 + get_expr(expr)
    elif expr[cur_idx] == "-":
        cur_idx += 1
        return term_1 - get_expr(expr)

    return term_1

def evaluate(expr: str):
    if expr is None or len(expr) == 0:
        print("Пустое выражение")
        return
    else:
        if is_bracket_valid(expr):
            return get_expr(expr)
        else:
            print("Несоответсвие закрытых и открытых скобок")
            return
    

while True:
    expr = input("Введите выражение для вычисления (для выхода - 'x')? ")
    if expr == 'x':
        break
    print(f"= {evaluate(expr)}")
    cur_idx = 0
