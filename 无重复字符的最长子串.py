"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

示例 4:
输入: s = ""
输出: 0

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        max_len = 0
        t = []
        for i in range(length):
            if s[i] not in t:
                t.append(s[i])
                if len(t) > max_len:
                    max_len = len(t)
            else:
                for item in t:
                    t = t[1:]
                    if item == s[i]:
                        t.append(s[i])
                        break
                # 思考：else 下面的代码块（row 42~46）可以用以下代码来代替
                # t = t[t.index(s[i])+1:]
                # t.append(s[i])
        return max_len
