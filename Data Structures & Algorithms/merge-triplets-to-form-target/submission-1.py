class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        matched = set()

        for i in range(len(triplets)):
            keep = True
            for j in range(3):
                if triplets[i][j] > target[j]:
                    keep = False
                    break
            if keep == True:
                for j in range(3):
                    if triplets[i][j] == target[j]:
                        matched.add(j)
            
                
        return len(matched) == 3


                    
                


