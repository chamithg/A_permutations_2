class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        '''
        this is the brute force solution, it checks if the permutation already in the result before appending.
        '''
        result = []
        def run(nums,perm):
            if not nums:
                result.append(perm)
            for i in range(len(nums)):
                if nums[i+1]!= nums[i]:
                    run(nums[:i]+nums[i+1:], perm+[nums[i]])
        
        run(nums,[])
        return result
        
obj = Solution()
nums = [1,1,2]
print(obj.permuteUnique(nums))