'''
코드를 더 아름답게 하는 방법은 없을까?

edge case를 아름답게 처리하기.
'''

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        share, remainder = divmod(abs(dividend), abs(divisor))

        answer_sign = (divisor < 0) == (dividend < 0)

        if answer_sign:
            answer = share
        else:
            answer = -share

        if answer > 2 ** 31 - 1:
            return 2 ** 31 - 1

        if answer < -2 ** 31:
            return -2 ** 31

        return answer


