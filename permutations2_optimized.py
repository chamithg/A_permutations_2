class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        '''
        in this solution, input is sorted and then prevent the recursive call on same elements
        '''
        nums.sort()
        result = []
        def run(nums,perm):
            
            if not nums:
                result.append(perm)
            for i in range(len(nums)):
                if i == 0 or nums[i]!=nums[i-1]:
                    run(nums[:i]+nums[i+1:], perm+[nums[i]])
        
        run(nums,[])
        return result
        
obj = Solution()
nums = [1,2,1]
print(obj.permuteUnique(nums))