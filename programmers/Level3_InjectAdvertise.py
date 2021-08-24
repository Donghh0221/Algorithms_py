## 0부터 쭉 가면서 시간대별 이용자 구하고
## 다시 0부터 쭉 가면서 이용시간 곱해서 최대인 출발 시간 구하기

import time


def solution(play_time, adv_time, logs):
    user_watch_timeline = []
    for play in logs:
        user_watch_timeline.append([get_sec(play.split('-')[0]),
                                    get_sec(play.split('-')[1])])

    user_watch_timeline = sorted(user_watch_timeline, key=lambda time: time[0])
    play_time_sec = get_sec(play_time)
    adv_time_sec = get_sec(adv_time)

    min_start_time = play_time_sec - adv_time_sec

    adv_start_time = 0
    total_watch_time = 0

    for user_watch_time in user_watch_timeline:
        start_candidate = user_watch_time[0]
        if min_start_time < start_candidate:
            break

        total_watch_time_of_candidate = get_total_watch_time(start_candidate, adv_time_sec, user_watch_timeline)

        if total_watch_time < total_watch_time_of_candidate:
            total_watch_time = total_watch_time_of_candidate
            adv_start_time = start_candidate

    return transform_sec_to_str(adv_start_time)


def get_total_watch_time(start_candidate, adv_time_sec, user_watch_timeline):
    total_watch_time = 0
    end_candidate = start_candidate + adv_time_sec
    for time in user_watch_timeline:
        if time[0] <= start_candidate <= time[1] <= end_candidate:
            total_watch_time += (time[1] - start_candidate)

        elif time[0] <= start_candidate and end_candidate <= time[1]:
            total_watch_time += adv_time_sec

        elif start_candidate <= time[0] and time[1] <= end_candidate:
            total_watch_time += (time[1] - time[0])

        elif start_candidate <= time[0] <= end_candidate <= time[1]:
            total_watch_time += (end_candidate - time[0])

    return total_watch_time


def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def transform_sec_to_str(sec):
    return time.strftime('%H:%M:%S', time.gmtime(sec))


if __name__ == "__main__":
    print(solution("02:03:55",
                   "00:14:15",
                   ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                    "01:37:44-02:02:30"]))
