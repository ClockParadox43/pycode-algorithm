# 题目链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# 利用哈希表记录是否出现过
# typing中的Counter是一个容器，而collections中的应该是一个类

from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0; l = 0;
        cnt = Counter();     # hashmap {char, int}
        for (r, c) in enumerate(s):
            cnt[c] += 1;
            while (cnt[c] > 1): cnt[s[l]] -= 1; l += 1;
            ans = max(r - l + 1, ans);
        return ans;