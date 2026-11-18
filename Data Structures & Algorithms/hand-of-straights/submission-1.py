class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False


        hand.sort()
        mp = {}
        for card in hand:
            mp[card] = mp.get(card, 0) + 1

        idx = 0
        for card in hand:
            if mp[card] == 0:
                continue
            for i in range(groupSize):
                if card + i not in mp or mp[card + i] <= 0:
                    return False
                else:
                    idx += 1
                    mp[card + i] -= 1

            
        return True






        