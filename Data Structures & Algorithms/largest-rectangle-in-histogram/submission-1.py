class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        st = [] #monotonic increasing, stores idx
        res = 0

        for i in range(len(heights)):
            while st and heights[st[-1]]>heights[i]:
                h = heights[st.pop()]

                if not st:
                    w = i
                else:
                    w = i-st[-1]-1
                res = max(res,h*w)
            st.append(i)
        return res