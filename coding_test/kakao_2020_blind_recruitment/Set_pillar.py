from copy import deepcopy


def solution(n, build_frame):
    current_state = []
    for build in build_frame:
        x, y, is_ceiling, is_building = build[0], build[1], build[2], build[3]
        if is_building:
            if is_ceiling and can_build_ceiling(x, y, current_state):
                current_state.append([x, y, is_ceiling])

            elif not is_ceiling and can_build_pillar(x, y, current_state):
                current_state.append([x, y, is_ceiling])

        else:
            if is_safety(x, y, is_ceiling, current_state) and [x, y, is_ceiling] in current_state:
                current_state = destroy(x, y, is_ceiling, current_state)

    answer = sorted(current_state, key=lambda x: (x[0], x[1], -x[2]))
    return answer

    '''
    1. 보가 (x, y)에 설치 가능한 조건
    -> (x + 1, y-1)가 기둥이거나
    -> (x, y-1)가 기둥이거나
    -> (x-1, y)와 (x+1, y)가 보거나
    '''


def can_build_pillar(x, y, current_state):
    if y == 0:
        return 1
    if [x, y - 1, 0] in current_state:
        return 1
    if [x, y, 1] in current_state:
        return 1
    if [x + 1, y, 1] in current_state:
        return 1
    return 0


def can_build_ceiling(x, y, current_state):
    if [x + 1, y - 1, 0] in current_state:
        return 1
    if [x, y - 1, 0] in current_state:
        return 1
    if [x - 1, y, 1] and [x + 1, y, 1] in current_state:
        return 1
    return 0


def is_safety(x, y, is_ceiling, current_state):
    after_remove = deepcopy(current_state)
    after_remove.remove([x, y, is_ceiling])
    for build in after_remove:
        test = deepcopy(after_remove)
        test.remove(build)

        test_x, test_y, test_is_ceiling = build[0], build[1], build[2]

        if test_is_ceiling:
            if not can_build_ceiling(test_x, test_y, test):
                return 0
        else:
            if not can_build_pillar(test_x, test_y, test):
                return 0
    return 1


def destroy(x, y, is_ceiling, current_state):
    current_state.remove([x, y, is_ceiling])
    return current_state


if __name__ == "__main__":
    build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                   [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

    print(solution(5, build_frame))
