import time


def solution(play_time, adv_time, logs):
    play_time_sec = get_seconds(play_time)
    ad_time_sec = get_seconds(adv_time)

    if ad_time_sec == play_time_sec:
        return '00:00:00'

    total_time = [0] * play_time_sec
    max_time = 0

    for log in logs:
        start = get_seconds(log.split("-")[0])
        end = get_seconds(log.split("-")[1])
        total_time[start] += 1
        total_time[end] -= 1

    for i in range(1, play_time_sec-1):
        total_time[i] = total_time[i] + total_time[i - 1]

    for i in range(1, play_time_sec-1):
        total_time[i] = total_time[i] + total_time[i - 1]

    for i in range(ad_time_sec-1, play_time_sec-1):
        if i >= ad_time_sec:
            max_time = max(max_time, total_time[i] - total_time[i - ad_time_sec])
        else:
            max_time = max(max_time, total_time[i])

    answer = time.strftime('%H:%M:%S', time.gmtime(max_time))

    return answer


def get_seconds(time_str):
    hh, mm, ss = time_str.split(':')
    return int(hh) * 3600 + int(mm) * 60 + int(ss)


if __name__ == "__main__":
    play_time = "02:03:55"
    adv_time = "00:14:15"
    logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    print(solution(play_time, adv_time, logs))
