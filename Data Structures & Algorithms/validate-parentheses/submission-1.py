class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if c=='{':
                st.append('}')
            elif c=='(':
                st.append(')')
            elif c=='[':
                st.append(']')
            else:
                if not st or c!=st.pop():
                    return False
        return len(st)==0
