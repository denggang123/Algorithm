from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        queue = [[item] for item in nums]
        while queue:
            item = queue[0]
            if len(item) != length:
                for num in nums:
                    if num not in item:
                        queue.append(item + [num])
                queue.pop(0)
            else:
                break
        return queue


print(Solution().permute([1, 2, 3]))
