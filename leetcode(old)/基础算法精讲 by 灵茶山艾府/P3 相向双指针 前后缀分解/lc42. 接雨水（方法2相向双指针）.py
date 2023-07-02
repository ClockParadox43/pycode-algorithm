# 题目分析:
#   一旦确定当前的最大高度，说明水起码不会从该高度流出去了
#   所以可以使用同向双指针，哪边的每次更新当前更底的高度
# 时间复杂度:O(n)
# 空间复杂度:O(1)

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0; l = 0; r = len(height) - 1;
        pre_max = 0; suf_max = 0;
        while (l < r):
            pre_max = max(pre_max, height[l]);      # 前缀最大值
            suf_max = max(suf_max, height[r]);
            if (pre_max < suf_max):
                ans += pre_max - height[l];         # 前缀最大值减去当前的高度
                l += 1;
            else: ans += suf_max - height[r]; r -= 1;
        return ans;