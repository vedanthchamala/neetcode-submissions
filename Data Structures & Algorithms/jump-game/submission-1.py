class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) 
        goal = n - 1
        for i in range(len(nums) - 2, -1, -1):
            for jump in range(1, nums[i] + 1):
                if i + jump == goal:
                    goal = i
                
        return True if goal == 0 else False

        
                    
                
             
            




                


        