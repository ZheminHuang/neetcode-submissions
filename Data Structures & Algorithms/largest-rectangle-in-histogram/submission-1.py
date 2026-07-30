class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # left[i]：i 左边第一个严格更矮的柱子
        left = [-1] * n

        # right[i]：i 右边第一个严格更矮的柱子
        right = [n] * n

        stack = []

        # 计算左边界
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                left[i] = stack[-1]

            stack.append(i)

        stack = []

        # 计算右边界
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            if stack:
                right[i] = stack[-1]

            stack.append(i)

        max_area = 0

        # 计算每根柱子作为矩形高度时的面积
        for i in range(n):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area