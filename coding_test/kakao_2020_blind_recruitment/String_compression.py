def solution(s):
    answer = len(s)
    maximum_length = len(s) // 2 + 1
    for i in range(1, maximum_length):
        idx = 0
        previous = ''
        count = 0
        compressed_string = ''
        while idx - i < len(s):
            next_sub_string = s[idx:idx + i]
            if previous == next_sub_string:
                count += 1
            else:
                if count == 0:
                    compressed_string += previous
                else:
                    compressed_string += str(count + 1)
                    compressed_string += previous
                previous = next_sub_string
                count = 0
            idx += i
        answer = min(len(compressed_string), answer)
    return answer


if __name__ == "__main__":
    solution('xababcdcdababcdcd')
