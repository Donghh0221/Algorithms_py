'''
a -> 선두 1시간 소모
b -> 후위 1시간 소모

a는 v의 가장 큰 값보다 크고
v의 가장 작은 값은 0보다 작은 동안,
매번 솔팅할 필요없이 max만 찾으면 되잖아
'''

def solution(v, a, b):
    additional_cost_for_first = a-b
    hours = 0
    while max(v) >= a and min(v) > 0:
        hours += 1
        v = [x-b for x in v]
        first_idx = v.index(max(v))
        v[first_idx] -= additional_cost_for_first
        print(v)
    return hours

v = [4,3,3]
a = 2
b = 1
print(solution(v, a, b))



