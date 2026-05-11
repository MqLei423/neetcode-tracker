import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_idx = len(nums)-k

        def quickselect(l,r):
            if l==r:
                return nums[r]

            pivot_i = random.randint(l,r)
            pivot = nums[pivot_i]

            p0,p1 = l,r
            cur = l

            while cur<=p1:
                if nums[cur]<pivot:
                    nums[p0],nums[cur] = nums[cur],nums[p0]
                    cur+=1
                    p0+=1
                elif nums[cur] > pivot:
                    nums[p1],nums[cur] = nums[cur],nums[p1]
                    p1-=1
                else:
                    cur+=1

            if target_idx<p0:
                return quickselect(l,p0-1)
            elif target_idx>p1:
                return quickselect(p1+1,r)
            else:
                return pivot
        
        return quickselect(0,len(nums)-1)     