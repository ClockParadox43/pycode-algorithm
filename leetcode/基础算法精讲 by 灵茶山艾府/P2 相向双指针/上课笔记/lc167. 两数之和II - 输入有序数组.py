# 思路1(暴力)：O(n^2)，每次判断是否去掉一个数的时间为O(n)
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