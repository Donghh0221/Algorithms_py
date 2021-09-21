import re

def solution(s):
    change_table = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for key in change_table.keys():
        s = re.sub(key, change_table[key], s)

    answer = int(s)
    return answer

if __name__ == "__main__":
    s = "23four5six7"
    print(solution(s))