from itertools import product, combinations


def dekart_proizv(dekart_expression: str, A: set, B: set, C: set) -> set:
    sets = {"A": A, "B": B, "C": C}
    return set(product(sets[dekart_expression[0]], sets[dekart_expression[2]]))


def powerset(S: set) -> set:
    res = set()
    for i in range(len(S) + 1):
        for elem in combinations(S, i):
            res.add(elem)
    return res


def solve(expression: str, A: set, B: set, C: set) -> set:
    expression = expression.replace("∩", "&").replace("∪", "|").replace("\\", "-").replace("∆", "^").replace("¯", "(A | B | C) - ").replace(" ", "")
    while "X" in expression:
        dekart_index = expression.index("X")
        dekart_res = dekart_proizv(expression[dekart_index-1:dekart_index+2], A, B, C)
        expression = expression[:dekart_index-1] + str(dekart_res) + expression[dekart_index+2:]
    return eval(expression)


if __name__ == "__main__":
    print(solve("(A & B) | C", {1, 4, 3}, {2, 3}, {5, 6}))
