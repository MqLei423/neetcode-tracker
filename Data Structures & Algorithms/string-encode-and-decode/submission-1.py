class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res+= str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        i,j = 0,0
        res = []

        while j < len(s):
            while s[j] != '#':
                j+=1

            length = int(s[i:j])
            res.append(s[j+1:j+length+1])
            i,j = j+length+1, j+length+1
        return res