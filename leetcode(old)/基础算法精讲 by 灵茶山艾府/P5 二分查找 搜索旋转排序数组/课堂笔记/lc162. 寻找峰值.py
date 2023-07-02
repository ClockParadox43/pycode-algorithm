# 题目链接:
#   https://leetcode.cn/problems/find-peak-element/
# 题目分析（类似上题二分的染色）:
#   定义：红色为峰顶左侧元素，蓝色为峰顶右侧元素或者峰顶。
#   由于峰顶一定存在数组中，所以数组最右侧一定是蓝色的。
#       - 所以初始化l=0, r=n-2
#   我们可以通过比较m和m+1的数字来进行染色，由于题目给定数字不同所以要么小于要么大于。
#
#   ps: 图解中的应该是闭区间写发，只是开区间的好理解。
#   关于闭区间：r就算是山峰也会找下去，所以最终如果返回r应返回r+1
from typing import List

# 开区间实现: [0, n-2] -> [-1, n-1]
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = -1; r = len(nums) - 1;
        while (l + 1 < r):
            m = (l + r) // 2;
            if (nums[m] > nums[m + 1]): r = m;  # 蓝色
            else: l = m;    # 红色
        return r;

# 闭区间实现
class Solution2:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0; r = len(nums) - 2;
        while (l <= r):
            m = (l + r) // 2;
            if (nums[m] > nums[m + 1]): r = m - 1; # 蓝色
            else: l = m + 1;    # 红色
        return l;