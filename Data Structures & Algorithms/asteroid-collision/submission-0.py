class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            destroyed = False
            while st and a<0 and st[-1]>0:
                toCollide = st.pop()
                if abs(toCollide)>abs(a):
                    destroyed = True
                    st.append(toCollide)
                    break
                if abs(toCollide)==abs(a):
                    destroyed = True
                    break
            if not destroyed:
                st.append(a)
        return st