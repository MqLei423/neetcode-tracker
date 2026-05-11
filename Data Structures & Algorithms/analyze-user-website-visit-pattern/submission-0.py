class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        logs = sorted(zip(timestamp,username,website))

        visits = defaultdict(list) #user->web
        for _,user,web in logs:
            visits[user].append(web)

        pattern_cnt = defaultdict(int)
        for user,sites in visits.items():
            n = len(sites)
            if n>=3:
                unique_pattern = set()
                for i in range(n-2):
                    unique_pattern.add((sites[i],sites[i+1],sites[i+2]))
                for pt in unique_pattern:
                    pattern_cnt[pt] += 1

        bestScore = max(pattern_cnt.values())
        res = []
        for k,v in pattern_cnt.items():
            if v==bestScore:
                res.append(k)
        res.sort()

        return list(res[0])