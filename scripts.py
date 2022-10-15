from itertools import product, combinations


def find_sets(start_index: int, expression: str, sets: dict) -> list:
    """Находит множества слева и справа от оператора

    :param start_index: Индекс оператора
    :param expression: все выражение, по которому выполняется поиск
    :param sets: словарь с введенными словарями A, B, C

    :return левое и правое множества, конечные индексы этих множеств ИЛИ ошибку:"""
    # левое множество
    set_index_left = 0
    if expression[start_index - 1] in ["A", "B", "C"]:
        first_u = sets[expression[start_index - 1]]
    elif expression[start_index - 1] == "}":
        set_index_left = 1
        while expression[start_index - 1 - set_index_left] != "{":
            if expression[start_index - 1 - set_index_left] == "}" or (start_index - 1 - set_index_left) == 0:
                return ["error", "Ошибка в записи первого множества в декартовом произведении"]
            set_index_left += 1
        first_u = eval(expression[start_index - 1 - set_index_left:start_index])
    else:
        return ["error", "Ошибка в записи первого множества в декартовом произведении"]

    # правое множество
    set_index_right = 0
    if expression[start_index + 1] in ["A", "B", "C"]:
        second_u = sets[expression[start_index + 1]]
    elif expression[start_index + 1] == "{":
        set_index_right = 1
        max_len = len(expression)
        while expression[start_index + 1 + set_index_right] != "}":
            if expression[start_index + 1 + set_index_right] == "{" or (start_index + 1 + set_index_right) == max_len:
                return ["error", "Ошибка в записи второго множества в декартовом произведении"]
            set_index_right += 1
        second_u = eval(expression[start_index + 1:start_index + 2 + set_index_right])
    else:
        return ["error", "Ошибка в записи второго множества в декартовом произведении"]
    return [first_u, second_u, set_index_left, set_index_right]


def compose(a: set, b: set) -> list:
    """Композиция функций

    :param a: Левое множество пар типа tuple
    :param b: Правое множество пар типа tuple

    :return Статус выполнения и ошибка/множество результата:"""
    res = set()
    for i in a:
        if type(i) != tuple:
            return ["error", f"Некорректный элемент для композиции: {i}"]
        for j in b:
            if type(j) != tuple:
                return ["error", f"Некорректный элемент для композиции: {j}"]
            if i[1] == j[0]:
                res.add((i[0], j[1]))
    return ["ok", res]


def find_and_make_compose(expression: str, sets: dict) -> str or list:
    """По индексу находит в строке композицию и выполняет операцию

    :param expression: Выражение целиком
    :param sets: словарь с введенными словарями A, B, C

    :return Новая строка выражения с результатом операции или ошибка:"""
    start_index = expression.index("◦")
    res_find_sets = find_sets(start_index, expression, sets)
    if res_find_sets[0] == "error":
        return res_find_sets

    first_u, second_u, set_index_left, set_index_right = res_find_sets
    compose_res = compose(first_u, second_u)
    if compose_res[0] == "error":
        return compose_res
    compose_res = compose_res[1]
    expression = expression[:start_index - 1 - set_index_left] + str(compose_res) + expression[start_index + 2 + set_index_right:]
    return expression


def dekart_proizv(expression: str, sets: dict) -> str or list:
    dekart_index = expression.index("X")
    res_find_sets = find_sets(dekart_index, expression, sets)
    if res_find_sets[0] == "error":
        return res_find_sets

    first_u, second_u, set_index_left, set_index_right = res_find_sets
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
    expression = expression.replace("∩", "&").replace("∪", "|").replace("\\", "-").replace("∆", "^").replace("¯", "(A | B | C) - ").replace(" ", "").replace(";", ",")
    if expression.count("}") != expression.count("{"):
        return ["error", "Проблема с определением множеств. Количество открывающихся и закрывающихся скобок не равно"]
    try:
        # Декартово произведение
        while "X" in expression:
            expression = dekart_proizv(expression, sets)
            if expression[0] == "error":
                return expression

        # Композиция
        while "◦" in expression:
            expression = find_and_make_compose(expression, sets)
            if expression[0] == "error":
                return expression

    except SyntaxError:
        return ["error", "Ошибка в записи декартова произведения"]
    try:
        result = eval(expression)
        if str(result) == "set()":
            result = "{}"
        return ["ok", result]
    except TypeError:
        return ["error", "Использован неверный тип данных"]
    except SyntaxError:
        return ["error", "Синтаксическая ошибка"]
    except Exception:
        return ["error", "Непредвиденная ошибка"]

