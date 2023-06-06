# 题目链接：https://leetcode.cn/problems/minimum-size-subarray-sum/submissions/
# 窗口大小不固定的叫做双指针，窗口大小固定的叫做滑动窗口
# 思路1(暴力)：向左扩展。 -> O(n^2)
# 思路2：固定右端点，左端点扩展，当满足tar停止。 -> O(n)

# enumerate：指在字典上枚举、列举
# enumerate参数：可遍历/迭代的对象(如列表、字符串)
# enumerate用于在for循环中的计数，利用它可同时获得索引和值
# enumerate返回值：返回的是enumerate对象

# 写法1:

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        s = 0       # 初始化总和
        l = 0       # 左端点指针  [l,r]: 左闭右闭，下标从0开始
        for r, x in enumerate(nums):
            s += x
            while s - nums[l] >= target:      # 如果总和减去左端点大于等于tar
                s -= nums[l]
                l += 1
            if s >= target:      # 如果是满足大于tar的
                ans = min(ans, r - l + 1)     # 特殊值法确定 +1, -1, +0
        return ans if ans <= n else 0         # 类似三目运算

# 写法2:
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1; s = 0; l = 0;
        for (r, x) in enumerate(nums):
            s += x;
            while (s >= target):         # 当总和大于tar时才更新
                ans = min(ans, r - l + 1);
                s -= nums[l]; l += 1;
        return ans if ans <= n else 0
