"""
给你一个字符串 s，找到 s 中最长的回文子串。
示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

示例 3：
输入：s = "a"
输出："a"

示例 4：
输入：s = "ac"
输出："a"
"""


class Solution:

    def longestPalindrome(self, s: str) -> str:
        self.s = s
        self.length = len(s)
        max_len = 0
        res = ''
        if self.length == 1:
            return s
        for i, char in enumerate(s[:-1]):  # 找每个字符的最长回文子串
            num, value = self.get_num_value(i)
            if num > max_len:
                max_len = num
                res = value
        return res

    def get_num_value(self, ii):
        res1 = []
        if self.s[ii] == self.s[ii + 1]:
            res1.append(self.s[ii])
            res1.append(self.s[ii+1])
            j = 1
            while (ii - j >= 0 and ii + j + 1 < self.length):
                if self.s[ii - j] == self.s[ii + j + 1]:
                    res1.insert(0, self.s[ii - j])
                    res1.append(self.s[ii + j + 1])
                    j += 1
                else:
                    break
        res2 = [self.s[ii]]
        j = 1
        while (ii - j >= 0 and ii + j < self.length):
            if self.s[ii - j] == self.s[ii + j]:
                res2.insert(0, self.s[ii - j])
                res2.append(self.s[ii + j])
                j += 1
            else:
                break
        result = ''
        res = res1 if len(res1) >= len(res2) else res2
        for item in res:
            result += item
        return len(res), result
