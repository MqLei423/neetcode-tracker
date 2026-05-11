class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dic:
            self.dic[key] = [(timestamp,value)]
        else:
            self.dic[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        li = self.dic[key]
        l,r = 0,len(li)-1
        while l<=r:
            mid = (l+r)//2
            if li[mid][0] == timestamp:
                return li[mid][1]
            elif li[mid][0] < timestamp:
                l = mid+1
            else:
                r = mid-1
        if r>=0:
            return li[r][1]
        else:
            return ""
