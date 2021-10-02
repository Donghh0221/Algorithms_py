import collections
import heapq


class Solution1:
    def leastInterval(self, tasks, n) -> int:
        task_counter = collections.Counter(tasks)

        tasks_to_do = list(zip(task_counter.values(), task_counter.keys()))

        ready_que = []
        blocked = []
        for task in tasks_to_do:
            heapq.heappush(ready_que, (-task[0], task[1]))

        unit_time = 0
        while ready_que or blocked:
            unit_time += 1
            if ready_que:
                occupy_process = heapq.heappop(ready_que)
                handled_process = (occupy_process[0] + 1, occupy_process[1])
                if handled_process[0] < 0:
                    blocked.append([handled_process, unit_time + n])

            for blocked_process in blocked:
                if blocked_process[1] <= unit_time:
                    heapq.heappush(ready_que, blocked_process[0])
                    blocked.remove(blocked_process)

        return unit_time
