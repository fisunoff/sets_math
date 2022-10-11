from itertools import product, combinations


def dekart_proizv(expression: str, sets: dict) -> str or list:
    dekart_index = expression.index("X")
    # левое множество
    set_index_left = 0
    if expression[dekart_index - 1] in ["A", "B", "C"]:
        first_u = sets[expression[dekart_index - 1]]
    elif expression[dekart_index - 1] == "}":
        set_index_left = 1
        while expression[dekart_index - 1 - set_index_left] != "{":
            if expression[dekart_index - 1 - set_index_left] == "}" or (dekart_index - 1 - set_index_left) == 0:
                return ["error", "Ошибка в записи первого множества в декартовом произведении"]
            set_index_left += 1
        first_u = eval(expression[dekart_index - 1 - set_index_left:dekart_index])
    else:
        return ["error", "Ошибка в записи первого множества в декартовом произведении"]

    # правое множество
    set_index_right = 0
    if expression[dekart_index + 1] in ["A", "B", "C"]:
        second_u = sets[expression[dekart_index + 1]]
    elif expression[dekart_index + 1] == "{":
        set_index_right = 1
        max_len = len(expression)
        while expression[dekart_index + 1 + set_index_right] != "}":
            if expression[dekart_index + 1 + set_index_right] == "{" or (dekart_index + 1 + set_index_right) == max_len:
                return ["error", "Ошибка в записи второго множества в декартовом произведении"]
            set_index_right += 1
        index = expression[dekart_index + 1:dekart_index + 2 + set_index_right]
        second_u = eval(expression[dekart_index + 1:dekart_index + 2 + set_index_right])
    else:
        return ["error", "Ошибка в записи второго множества в декартовом произведении"]
    dekart_res = set(product(first_u, second_u))
    expression = expression[:dekart_index - 1 - set_index_left] + str(dekart_res) + expression[dekart_index + 2 + set_index_right:]
    return expression


def powerset(S: set) -> set:
    res = set()
    for i in range(len(S) + 1):
        for elem in combinations(S, i):
            res.add(elem)
    return res


def solve(expression: str, A: set, B: set, C: set) -> set or list:
    sets = {"A": A, "B": B, "C": C}
    expression = expression.replace("∩", "&").replace("∪", "|").replace("\\", "-").replace("∆", "^").replace("¯", "(A | B | C) - ").replace(" ", "")
    try:
        while "X" in expression:
            expression = dekart_proizv(expression, sets)
            if expression[0] == "error":
                return expression
    except SyntaxError:
        return ["error", "Ошибка в записи декартова произведения"]
    try:
        return eval(expression)
    except TypeError:
        return ["error", "Использован неверный тип данных"]


if __name__ == "__main__":
    print(solve("(A & B) | C", {1, 4, 3}, {2, 3}, {5, 6}))
