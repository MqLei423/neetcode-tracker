class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        foundA,foundB,foundC = False,False,False
        x,y,z = target

        for a,b,c in triplets:
            if a>x or b>y or c>z:
                continue
            
            if a==x:
                foundA = True
            if b==y:
                foundB = True
            if c==z:
                foundC = True
            
            if foundA and foundB and foundC:
                return True
        return foundA and foundB and foundC