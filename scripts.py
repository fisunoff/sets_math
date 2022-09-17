def solve(expression: str, A: set, B: set, C: set) -> set:
    expression = expression.replace("∩", "&").replace("∪", "|").replace("\\", "-").replace("∆", "^")
    return eval(expression)


if __name__ == "__main__":
    print(solve("(A & B) | C", {1, 4, 3}, {2, 3}, {5, 6}))
