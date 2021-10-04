from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for start_idx in range(len(gas)):
            tank = 0
            tank += gas[start_idx]
            for idx in range(start_idx, start_idx+len(gas)):
                tank -= cost[idx % len(gas)]
                if tank < 0:
                    break

                tank += cost[(idx + 1) % len(gas)]

            tank -= gas[start_idx]
            if -1 < tank:
                return 0
        return -1
