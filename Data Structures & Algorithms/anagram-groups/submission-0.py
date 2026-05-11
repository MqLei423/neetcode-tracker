class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c)-ord('a')]+=1
            d[tuple(freq)].append(s)
        
        res = []
        for v in d.values():
            res.append(v)
        return res