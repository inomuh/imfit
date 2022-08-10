class Solution:
    def largestRectangleArea(heights) -> int:
        maxArea = 0
        stack = []  # pair: (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append( ))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea

print(Solution.largestRectangleArea(heights = [2,4]))