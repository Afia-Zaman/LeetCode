class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        a = 0
        n = (len(nums))
        nums_n = [nums[0]]
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums_n.append(nums[i])
              
        for i in range (1, len(nums_n )-1):
            if nums_n[i] > nums_n[i-1] and nums_n[i] > nums_n[i+1]:
                a += 1
            elif nums_n[i] < nums_n[i-1] and nums_n[i] < nums_n[i+1]:
                a += 1          
        return a

nums = [2,4,1,1,6,5]
print(Solution.countHillValley(nums))
