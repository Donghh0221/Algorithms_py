from collections import deque

def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    lower_cities = list(map(lambda x: x.lower(), cities))

    if cacheSize == 0:
        return len(lower_cities) * 5

    for city in lower_cities:
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            if len(cache) < cacheSize or len(cache) == 0:
                cache.append(city)
                answer += 5
            else:
                cache.popleft()
                cache.append(city)
                answer += 5
    return answer


if __name__ == "__main__":
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]	))
