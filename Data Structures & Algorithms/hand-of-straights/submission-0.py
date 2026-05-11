class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for card in sorted(hand):
            if count[card] == 0:
                continue
            
            hand_n = count[card]
            for i in range(card,card+groupSize):
                if count[i] < hand_n:
                    return False
                count[i]-=hand_n
        return True