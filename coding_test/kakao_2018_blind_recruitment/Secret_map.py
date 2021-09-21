def solution(n, arr1, arr2):
    answer = []
    for pair in zip(arr1, arr2):
        wall = pair[0] | pair[1]
        bit_wall = bit_transformer(n, wall)
        wall = bit_wall.replace("0", " ").replace("1", "#")
        answer.append(wall)
    return answer


def bit_transformer(bit_length, number):
    return f'{number:0{bit_length}b}'


def test_bit_transformer():
    assert '01001' == bit_transformer(5, 9)
    assert '10100' == bit_transformer(5, 20)


if __name__ == "__main__":
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]
    print(solution(n, arr1, arr2))
