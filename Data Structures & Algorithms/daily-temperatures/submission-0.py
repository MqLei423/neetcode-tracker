class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []

        for i,t in enumerate(temperatures):
            while st and t>st[-1][1]:
                idx,_ = st.pop()
                res[idx] = i-idx
            st.append([i,t])
        return res
