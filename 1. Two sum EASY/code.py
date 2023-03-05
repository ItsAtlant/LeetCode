#rune time is too high
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for x in range (length):
            for y in range (length):
                try:
                    if nums[x] + nums[y] == target and x!=y:
                        return x,y
                except:
                    pass

