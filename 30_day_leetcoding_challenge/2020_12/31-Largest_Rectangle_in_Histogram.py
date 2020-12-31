class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(0)
        max_area = 0

        for index, value in enumerate(heights):
            while (stack and heights[stack[-1]] >= value):
                the_index = stack.pop()
                width = (index - stack[-1] - 1 if stack else index)
                max_area = max(max_area, heights[the_index]*width)
            stack.append(index)

        return max_area
