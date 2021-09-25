class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq


class Solution:
    def sortList(self, head: [ListNode]) -> [ListNode]:
        heap = []
        p = head
        while p:
            heapq.heappush(heap, p.val)
            p = p.next

        p = head

        while heap:
            value = heapq.heappop(heap)
            p.val = value
            p = p.next

        return head
