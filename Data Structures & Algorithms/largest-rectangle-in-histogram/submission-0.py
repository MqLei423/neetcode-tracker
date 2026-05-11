class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        st = [-1]
        res = 0

        for i in range(len(heights)):
            while st[-1] != -1 and heights[i] < heights[st[-1]]:
                h = heights[st.pop()]
                w = i-st[-1]-1
                res = max(res,h*w)
            st.append(i)
        return res