def parse_operators(expression):
    operators = []

    for lexeme in expression:
        if lexeme in '+-*/':
            operators.append(lexeme)

    return operators


def parse_operands(expression):
    operands = []
    digits = [str(i) for i in range(10)]

    for lexeme in expression:
        if lexeme in digits:
            operands.append(lexeme)

    return [int(op) for op in operands]


def solve(expression):
    operands = parse_operands(expression)
    operators = parse_operators(expression)

    if len(operators) > 1 and operators[1] in '*/' and operators[0] not in '*/':
        operators[0], operators[1] = operators[1], operators[0]
        operands = [*[op for op in operands[1:len(operands)]], -operands[0]]

        operators[1] = '-' if operators[1] == '+' else '-'

    result = operands[0]

    for i, operator in enumerate(operators):
        operand = operands[i + 1]

        if i == 1 and operator == '-':
            result *= -1

        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            result /= operand

    return result


file = open('lab7_v3_input.txt', 'r+')

expression = file.read()
file.write(f' = {str(solve(expression))}')

file.close()
