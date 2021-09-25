
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

def merge_sort_inner(data):
    def inner_merge(left, right):
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
    return inner_merge(left, right)



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

def quick_sort_left_pivot(data):
    # less랑 greater를 새로 생성해야해서 메모리 비용이 추가될 듯?
    if len(data) < 1:
        return data
    else:
        pivot = data[0]
        less = [x for x in data[1:] if x <= pivot]
        greater = [x for x in data[1:] if x > pivot]
        return quick_sort_left_pivot(less) + [pivot] + quick_sort_left_pivot(greater)

import time
import random
data = list(range(-100000, 100000))
random.shuffle(data)

start = time.time()
merge_sort(data)
end = time.time()
print(f"{end - start:.5f} sec")
start = time.time()
merge_sort_inner(data)
end = time.time()
print(f"{end - start:.5f} sec")
start = time.time()
quick_sort_left_pivot(data)
end = time.time()
print(f"{end - start:.5f} sec")
start = time.time()
quick_sort_lomuto_pivot(data, 0, len(data)-1)
end = time.time()
print(f"{end - start:.5f} sec")
