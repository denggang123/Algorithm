from typing import List

"""https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        prev = None
        dup_num = 0
        for index in range(length):
            if nums[index - dup_num] == prev:
                dup_num += 1
                nums.pop(index - dup_num + 1)
            else:
                prev = nums[index - dup_num]
        return len(nums)


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


print(Solution2().removeDuplicates([1, 1, 1, 2, 3, 4, 4, 4, 5, 5, 6]))
