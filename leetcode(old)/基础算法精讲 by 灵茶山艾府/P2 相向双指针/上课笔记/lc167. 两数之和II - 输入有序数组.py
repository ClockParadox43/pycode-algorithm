# 题目链接：
# https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
# 思路1(暴力)：O(n^2)，每次判断是否去掉一个数的时间为O(n)
# 题目分析：由于题目给定序列为单调递增，所以l,r相加后的数字一定也是具有单调性的（每次控制一个端点的情况），
#         将数组元素放到平面直接坐标系上看，控制两个端点的趋势，使得端点的x轴和tar的x轴相等即可。
# 思路2：l,r分别指向左右端点，如果w[l]+w[r]>tar则r--,如果w[l]+w[r]<tar则l++
#       时间复杂度：O(n)，每次花费O(1)的时间排除一个数，所以整体是O(n)

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0; r = len(numbers) - 1;
        while (l < r):
            if (numbers[l] + numbers[r] == target): break;
            if (numbers[l] + numbers[r] > target): r -= 1;
            if (numbers[l] + numbers[r] < target): l += 1;
        return [l + 1, r + 1];