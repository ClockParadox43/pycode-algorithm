# 题目链接:
#   https://leetcode.cn/problems/container-with-most-water/
# 题目分析:
#   由题意可以发现，是否能盛水，取决于两边木板的高度
#   所以我们只需开两个前后缀最大高度的数组，前缀后缀取最小，因为只有低于高度的水才会流出去
#   有 该高度的木板-当前高度的木板=水的容量，最后将水的容量累加起来即可
# 时间复杂度: O(n)
# zip(): 将迭代对象转化成参数，将对象中对应的元素打包成元祖，
#        如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
#           - 返回值: 由这些元祖组成的对象。
#           - 优点: 节约内存
#           - 我们可以使用 list() 转换来输出列表。
# range(p1, p2, p3):
#       - [p1,p2): 左闭右开确定范围
#       - p3: 确定步长

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height);
        pre_max = [0] * n; pre_max[0] = height[0];      # 开长度为n的数组
        for (i) in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i]);
        suf_max = [0] * n; suf_max[-1] = height[-1];
        for (i) in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i]);
        ans = 0;
        for (h, pre, suf) in zip(height, pre_max, suf_max):
            ans += min(pre, suf) - h;
        return ans;