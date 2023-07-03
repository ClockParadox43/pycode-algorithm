# 更多二分题目（二分题单）：
#   https://leetcode.cn/problems/search-in-rotated-sorted-array/
# 题目分析:
#
#   方法2: 分类讨论，如果mid在target及其右侧 -> 蓝色
#           1. 如果mid>最后一个数
#                   - 说明mid在第一段，如果此时target>最后一个数，说明mid和target在同一段。
#                     如果此时mid>=target，说明mid在target的右边 -> 蓝色
#           2. 如果mid≤最后一个数，
#                   - 说明mid在第二段，如果此时target>=mid并且target>最后一个数，
#                     那么target就在第一段。 -> 蓝色
#           3. 其余就是红色的情况


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_blue(i: int) -> bool:  # 判断mid是否在target的右侧
            ed = nums[-1];
            if (nums[i] > ed):  # 说明在第一段，如果tar也在第一段并且mid>tar就可以染成蓝色
                return target > ed and nums[i] >= target;
            else:               # nums[i] < ed: 说明mid在二段，如果tar>ed，tar在第一段直接蓝色，如果mid>=tar，说明mi在tar右边
                return target > ed or nums[i] >= target;

        l = -1; r = len(nums);
        while (l + 1 < r):
            m = (l + r) // 2;
            if (is_blue(m)): r = m;
            else: l = m;
        if r == len(nums) or nums[r] != target: return -1;
        else: return r;