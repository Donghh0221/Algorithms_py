current = 0
answer = 0

for a in range(10):
    num_unload, num_ride = list(map(int, input().split()))
    current += num_ride
    current -= num_unload
    answer = max(current, answer)

print(answer)
