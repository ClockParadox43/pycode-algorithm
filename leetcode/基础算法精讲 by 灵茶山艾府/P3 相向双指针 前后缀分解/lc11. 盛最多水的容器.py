# 题目链接:
#   https://leetcode.cn/problems/trapping-rain-water/
# 题目分析:
#   用双向双指针不难看出，底边单调递减，所以我们在底边尽可能长的同时，让高度尽可能长
#   因为高度并不满足单调性，所以每次排除掉高度较短的一边
#   因为面积是由于底和高一起决定的，面积不满足单调性，所以这个过程的答案需要都看一遍
# 时间复杂度:
#   因为每次移动指针的时间为O(1)，所以整体的时间复杂度为O(n)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0; r = len(height) - 1; ans = 0;
        while (l < r):
            area = (r - l) * min(height[l], height[r]);
            if (height[l] > height[r]): r -= 1;     # 让高度尽可能大
            else: l += 1;
            ans = max(ans, area);
        return ans;