class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        var = {}
        for i in range(len(nums)):
            value = target - nums[i]
            if value in var:
                return [var[value][1], i]
            else:
             var[nums[i]] = [(target - nums[i]),i]
