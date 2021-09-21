'''
옆자리랑 계속 비교하면서 줄여나감
'''


def bubble_sort(data):
    for i in range(1, len(data)):
        for j in range(0, len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def test_bubble():
    a = [3, 2, 1, 4, 5]
    b = [4, 3, 1, 2, 6, 7, 5]
    assert bubble_sort(a) == [1, 2, 3, 4, 5]
    assert bubble_sort(b) == [1, 2, 3, 4, 5, 6, 7, ]


'''
계속 쭉 훑으면서 가장 작은 애를 가장 앞으로 땡겨오는 것
'''


def selection_sort(data):
    for i in range(len(data) - 1):
        minimum_idx = i
        for j in range(i + 1, len(data)):
            if data[minimum_idx] > data[j]:
                minimum_idx = j
        data[i], data[minimum_idx] = data[minimum_idx], data[i]
    return data


def test_selection():
    a = [3, 2, 1, 4, 5]
    b = [4, 3, 1, 2, 6, 7, 5]
    assert selection_sort(a) == [1, 2, 3, 4, 5]
    assert selection_sort(b) == [1, 2, 3, 4, 5, 6, 7, ]


def insert_sort(data):
    for key in range(1, len(data)):
        for j in range(key, 0, -1):
            if data[j - 1] > data[j]:
                data[j], data[j - 1] = data[j - 1], data[j]
    return data


def test_insert():
    a = [3, 2, 1, 4, 5]
    b = [4, 3, 1, 2, 6, 7, 5]
    assert insert_sort(a) == [1, 2, 3, 4, 5]
    assert insert_sort(b) == [1, 2, 3, 4, 5, 6, 7]


def merge(left, right):
    if not left or not right:
        return left or right
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])

    return result


def merge_sort(data):
    if len(data) < 2:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)


def test_merge():
    a = [3, 2, 1, 4, 5]
    b = [4, 3, 1, 2, 6, 7, 5]
    assert merge_sort(a) == [1, 2, 3, 4, 5]
    assert merge_sort(b) == [1, 2, 3, 4, 5, 6, 7, ]


def quick_sort(data):
    pass


def heap_sort(data):
    pass


def tim_sort(data):
    pass


def count_sort(data):
    pass
