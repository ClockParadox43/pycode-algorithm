# 题目链接:
#   https://leetcode.cn/problems/trapping-rain-water/
# 题目分析:
#   底边满足单调性，高度并不满足，因为盛水的高度取决于最短的那根柱子，为了使面积尽可能大，
#   所以 l,r 哪边短就移动哪边。面积是由于底和高一起决定，面积不满足单调性，所以这个过程的答案需要都看一遍
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