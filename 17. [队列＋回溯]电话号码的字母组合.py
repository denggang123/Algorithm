class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        if not digits:
            return []
        phone = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        queue = ['']
        for digit in digits:
            letters = phone[ord(digit) - 50]
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in letters:
                    queue.append(tmp + letter)
        return queue


class Solution2:
    def letterCombinations(self, digits: str) -> [str]:
        if not digits:
            return []

        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(conbination, nextdigit):
            if len(nextdigit) == 0:
                res.append(conbination)
            else:
                for letter in phone[nextdigit[0]]:
                    backtrack(conbination + letter, nextdigit[1:])

        res = []
        backtrack('', digits)
        return res


print(Solution2().letterCombinations("23"))
