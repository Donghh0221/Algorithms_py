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


def merge_sort(data):
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
    assert merge_sort(b) == [1, 2, 3, 4, 5, 6, 7]


def quick_sort_lomuto_pivot(data, lo, hi):
    def partition(lo, hi):
        pivot = data[hi]
        left = lo
        for right in range(lo, hi):
            if data[right] < pivot:
                data[left], data[right] = data[right], data[left]
                left += 1
        data[left], data[hi] = data[hi], data[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        quick_sort_lomuto_pivot(data, lo, pivot - 1)
        quick_sort_lomuto_pivot(data, pivot + 1, hi)
    return data


def test_quick_sort_lomuto_pivot():
    a = [3, 2, 1, 4, 5]
    b = [4, 3, 1, 2, 6, 7, 5]
    assert quick_sort_lomuto_pivot(a, 0, len(a) - 1) == [1, 2, 3, 4, 5]
    assert quick_sort_lomuto_pivot(b, 0, len(b) - 1) == [1, 2, 3, 4, 5, 6, 7]


def quick_sort_left_pivot(data):
    # less랑 greater를 새로 생성해야해서 메모리 비용이 추가될 듯?
    if len(data) < 1:
        return data
    else:
        pivot = data[0]
        less = [x for x in data[1:] if x <= pivot]
        greater = [x for x in data[1:] if x > pivot]
        return quick_sort_left_pivot(less) + [pivot] + quick_sort_left_pivot(greater)


def test_quick_sort_left_pivot():
    a = [3, 2, 1, 4, 5]
    b = [4, 3, 1, 2, 6, 7, 5]
    assert quick_sort_left_pivot(a) == [1, 2, 3, 4, 5]
    assert quick_sort_left_pivot(b) == [1, 2, 3, 4, 5, 6, 7]


import heapq


def heap_sort_with_heappush(data):
    sorted_data = []
    heapq.heapify(data)

    while data:
        sorted_data.append(heapq.heappop(data))

    return sorted_data


def heap_sort_with_heapify(data):
    heap = []
    sorted_data = []

    for number in data:
        heapq.heappush(heap, number)

    while heap:
        sorted_data(heapq.heappop(heap))

    return sorted_data


def tim_sort(data):
    pass


def count_sort(data):
    pass
