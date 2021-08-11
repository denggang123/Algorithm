

class Solution:
    """kerwin's solution"""
    @staticmethod
    def reverse(x: int) -> int:
        flag = 1 if x > 0 else -1
        x = abs(x)
        stack = []
        while True:
            if x // 10:
                x, res = x // 10, x % 10
                stack.append(res)
            else:
                stack.append(x)
                break
        result = 0
        for i, val in enumerate(reversed(stack)):
            if val:
                result += val * 10**i
        if result > pow(2, 31) - 1 or result < - pow(2, 31):
            return 0
        return flag * result
