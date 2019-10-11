class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        
        if len(hand) % W != 0:
            return False
        if W == 1:
            return True
        
        hand.sort()
        
        while len(hand) > 0:
            n = hand.pop(0)
            for i in range(1,W):
                if n+i in hand:
                    hand.pop(hand.index(n+i))
                else:
                    return False
        
        return True
                    

