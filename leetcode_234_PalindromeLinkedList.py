from collections import deque

class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool :
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        q: deque = deque()
        if not head:
            return True

        node = head
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True



class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        q: list = []
        if not head:
            return True

        node = head

        while node is not None:
            q.append(node.val)
            node = node.next

        print(q)

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True




if __name__ == '__main__':
    S = Solution()
    head = ListNode([1,2])
    print(S.isPalindrome(head))
