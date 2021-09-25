'''
1. (()[[]])([])
2. (2[3])(3)
3. (2 9) 6
4. (11) 6
5. 22 6
6. 28
'''
숫자 숫자 만나면 +
def calculate_stack_value(l:list) -> int:
    stack = []
    while l:
        s = l.pop(0)
        if not stack:
            stack.append(s)
        else:
            if stack[-1] == "(" and s == ")":
                stack.pop()
                l.insert(0, 2)
            elif stack[-1] == "[" and s == "]":
                stack.pop()
                l.insert(0, 3)
            elif stack[-1] == "[" or "(" and


        l.insert(0, value)


def check_right_string(string: str):
    stack = []
    for s in string:
        if stack and stack[-1] == "(" and s == ")":
            stack.pop()
        elif stack and stack[-1] == "[" and s == "]":
            stack.pop()
        else:
            stack.append(s)
    if len(stack) == 0:
        return True

    return False


def test_check_right_string():
    assert check_right_string("(()[[]])([])")
    assert not check_right_string("[][]((])")
