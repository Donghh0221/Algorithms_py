def solution(stones, k):
    answer = min(stones)
    count = 0
    while True:
        for stone in stones:
            if stone <= answer:
                count += 1
                if count >= k:
                    return answer
            else:
                count = 0
        answer += 1
        count = 0



if __name__ == "__main__":
    stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
    k = 3
    print(solution(stones, k))