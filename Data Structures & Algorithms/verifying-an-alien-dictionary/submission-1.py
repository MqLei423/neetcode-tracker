class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = defaultdict(int)
        for i,c in enumerate(order):
            dic[c] = i
        
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            tie = True
            for j in range(min(len(w1),len(w2))):
                if dic[w1[j]] > dic[w2[j]]:
                    return False
                if dic[w1[j]] < dic[w2[j]]:
                    tie = False
                    break
            if tie and len(w1) > len(w2):
                return False
        
        return True
