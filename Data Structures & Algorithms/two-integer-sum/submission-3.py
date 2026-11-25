class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_map = {}
        for i, num in enumerate(nums):
            c = target - num
            if c in freq_map:
                return[freq_map[c], i]
            freq_map[num] = i
