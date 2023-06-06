# 题目链接：https://leetcode.cn/problems/subarray-product-less-than-k/
# 上一道题是在while不满足要求的情况下，相反，while还可以变得满足要求
#
# 具体方法和209一样，子数组的数目如何计算？
#   例：[10,5,2,6]
#   假设枚举到2，需要算的就是以2为右端点满足要求的子数组个数，所以直接求递推公式
#   [l,r]我们需要计算以r为右端点子数组的个数
#   如果从[l,r]这段子数组是小于k的，那么[l+1,r],[l+2,r]...[r,r]这些子数组也一定是小于k的
#   其中子数组的个数就是[l,r]的元素个数
#   ps：这里子数组数量指的是必须包含右端点的子数组的数量

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0;
        ans = 0; prod = 1; l = 0; # 乘积等于1
        for (r, x) in enumerate(nums):
            prod *= x;
            while (prod >= k): prod /= nums[l]; l += 1;     # 不满足条件时缩小
            ans += r - l + 1;
        return ans;