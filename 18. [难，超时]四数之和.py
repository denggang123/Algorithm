class Solution1:
    def fourSum(self, nums, target):
        res_list = list()
        length = len(nums)
        for i1 in range(length):
            for i2 in range(i1 + 1, length):
                for i3 in range(i2 + 1, length):
                    for i4 in range(i3 + 1, length):
                        temp = sorted([nums[i1], nums[i2], nums[i3], nums[i4]])
                        if temp not in res_list and temp[0] + temp[1] + temp[2] + temp[3] == target:
                            res_list.append(temp)
        return res_list


class Solution2:
    def fourSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                d.setdefault(nums[i] + nums[j], []).append((i, j))
        result = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for a, b in d.get(target - nums[i] - nums[j], []):
                    temp = {i, j, a, b}
                    if len(temp) == 4:
                        result.add(tuple(sorted(nums[t] for t in temp)))
        return [list(item) for item in result]


if __name__ == '__main__':
    nums = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 20, 20, 20, 20, 20, 20, 20,
            20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30,
            30, 30, 30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 50,
            50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 60, 60, 60, 60, 60, 60, 60, 60,
            60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70,
            70, 70, 70, 70, 70, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 90, 90,
            90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90]
    target = 200
    import time
    time1 = time.time()
    res1 = Solution1().fourSum(nums, target)
    time2 = time.time()
    time3 = time.time()
    res2 = Solution2().fourSum(nums, target)
    time4 = time.time()

    """BF time: 27.982453107833862
    other's time: 16.112895488739014
    True"""
    print("BF time: {}".format(time2 - time1))
    print("other's time: {}".format(time4 - time3))
    print(len(res1) == len(res2))
