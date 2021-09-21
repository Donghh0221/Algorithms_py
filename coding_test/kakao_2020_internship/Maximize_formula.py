import re
from itertools import permutations


def solution(expression):
    answer = 0
    orders = permutations('*+-', 3)
    separated = separator(expression)
    for order in orders:
        priority_table = dict(zip(order, [0, 1, 2]))

        stack = []
        postfix = []
        for obj in separated:
            if type(obj) is int:
                postfix.append(obj)
            else:
                while stack and priority_table[stack[-1]] <= priority_table[obj]:
                    postfix.append(stack.pop())
                stack.append(obj)

        postfix += reversed(stack)
        stack = []
        for obj in postfix:
            if obj == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif obj == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif obj == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            else:
                stack.append(obj)
        answer = max(answer, abs(stack[0]))

    return answer

def separator(expression):
    separated = []
    while expression:
        num = re.search('\d+', expression)
        if num.start() == 0:
            separated.append(int(expression[num.start():num.end()]))
            expression = expression[num.end():]
        else:
            op = re.search('[^0-9]', expression)
            separated.append(expression[op.start():op.end()])
            expression = expression[op.end():]
    return separated


if __name__ == "__main__":
    expression = "50*6-3*2"
    print(solution(expression))
