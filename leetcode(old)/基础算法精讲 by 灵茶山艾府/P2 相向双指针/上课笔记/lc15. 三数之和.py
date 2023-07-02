# 题目链接:
#   https://leetcode.cn/problems/3sum/submissions/
# 由题意:
#   1.三数之和顺序并不重要
#   2.满足: i < j < k (题目说!=)，所以只要枚举i,如果 j+k == ~i，即可
#   3.答案中不能包含重复的三元组：只要当前枚举的数和上一个数是相同的直接跳过即可
# 思路:
#   确定i的范围. 枚举[l,r]是否等于-nums[i]
# 枚举范围:
#   下标r占位n-1, 下标l占位n-2，那么i枚举到n-3即可,因为range是开区间，枚举到n-2
# 像[-1,-1,2]这样的测试用例会不会跳过被过滤掉？
#   - 不会，因为i和[l,r]不是同一个循环中的
# 时间复杂度:
#   排序: O(nlogn)
#   枚举i: O(n), 双指针: o(n)
#   所以整个循环等于O(n^2)
#   由于O(n^2) > O(nlogn) 所以整体的时间复杂度为 O(n^2)

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort();
        n = len(nums); ans = [];
        for (i) in range(n - 2):
            if (i > 0 and nums[i] == nums[i - 1]): continue;        # 去重
            if (nums[i] + nums[i + 1] + nums[i + 2] > 0): break;    # 优化1
            if (nums[i] + nums[-2] + nums[-1] < 0): continue;       # 优化2
            l = i + 1; r = n - 1;
            while (l < r):
                s = nums[i] + nums[l] + nums[r];
                if (s > 0): r -= 1;
                elif (s < 0): l += 1;
                else:       # 加完后还[l,r]的范围可能还会有符合条件的，将重复的跳过
                    ans.append([nums[i], nums[l], nums[r]]);
                    l += 1;
                    while (l < r and nums[l] == nums[l - 1]): l += 1
                    r -= 1;
                    while (r > l and nums[r] == nums[r + 1]): r -= 1
        return ans;
