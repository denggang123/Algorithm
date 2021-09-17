from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        length = len(nums)
        fast = slow = 0
        while fast < length:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


nums = [1, 2, 4, 5, 7, 5]
val = 5
print(Solution().removeElement(nums, val))
print(nums)



