class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        str_map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for item in s:
            if stack:
                try:
                    if str_map[stack[-1]] == item:
                        stack.pop(-1)
                    else:
                        stack.append(item)
                except:
                    return False
            else:
                stack.append(item)
        return True if not stack else False


print(Solution().isValid("([])"))
