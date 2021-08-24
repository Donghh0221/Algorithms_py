class Solution1:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            print(f'left is {left}, right is {right}')
            print(f'left_max is {left_max}, right_max is {right_max}, volume = {volume}')
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1

        return volume

class Solution2:
    def trap(self, height: list[int]) -> int:
        stack = []
        volume = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                if not len(stack):
                    break
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
            print(stack)
        return volume

if __name__ == '__main__':
    S = Solution2()
    print(S.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
