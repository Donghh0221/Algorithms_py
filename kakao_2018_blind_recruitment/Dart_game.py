import re


def solution(dartResult):
    operand, operator = parser(dartResult)
    answer = calculator(operand, operator)
    return answer

def calculator(operand, operator):
    terms = [0]*3
    for i in range(3):
        terms[i] = operand[i]
        if operator[i][0] == "S":
            terms[i] = terms[i]
        elif operator[i][0] == "D":
            terms[i] = terms[i]**2
        elif operator[i][0] == "T":
            terms[i] = terms[i] ** 3

        if len(operator[i]) > 1:
            if operator[i][1] == "#":
                terms[i] = -terms[i]
            else:
                terms[i] *= 2
                if i in (1, 2):
                    terms[i-1] *= 2
    return sum(terms)

def test_calculator():
    assert 37 == calculator([1,2,3], ['S', 'D*', 'T'])
    assert 9 == calculator([1, 2, 10], ['D', 'S#', 'S'])

def parser(dartResult):
    operator = re.split('[0-9]+', dartResult)[1:]
    operand = list(map(int, re.findall('[0-9]+', dartResult)))
    return operand, operator


def test_parser():
    operand, operator = parser('1S2D*3T')
    assert operand == [1, 2, 3]
    assert operator == ['S', 'D*', 'T']

if __name__ == "__main__":
    print(solution("1D2S3T*"))