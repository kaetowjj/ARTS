class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {} # val : index
        for i,j in enumerate(nums):
            diff = target - j
            if diff in prevmap:
                return [prevmap[diff], i]
            prevmap[j] = i
        return
        