from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        word_num = len(words)
        sub_len = word_len * word_num
        s_len = len(s)
        p = 0
        res = []
        while s_len - p >= sub_len:
            index_list = []
            for i in range(word_num):
                target = s[p + i * word_len: p + (i + 1) * word_len]
                for index, item in enumerate(words):
                    if item == target:
                        if index in index_list:
                            continue
                        index_list.append(index)
                        break
            if sorted(index_list) == list(range(word_num)):
                res.append(p)
            p += 1
        return res


a = "wordgoodgoodgoodbestword"
b = ["word", "good", "best", "good"]
print(Solution().findSubstring(a, b))
