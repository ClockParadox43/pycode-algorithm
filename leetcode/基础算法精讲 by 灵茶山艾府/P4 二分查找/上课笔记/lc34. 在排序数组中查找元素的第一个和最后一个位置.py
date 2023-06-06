# 内容:
#   1.二分查找在 [], (), [), 上的写法
#   2.处理 ≥,≤,>,< 四种情况

# 二分查找:
#   保证闭区间 [L,R] 内的是不确定的，且 L-1 和 R+1 的是确定的，
#   关键不在于区间里的元素具有什么性质，而是区间外面的元素具有什么性质，只有这样才能根据循环不等式进行判断。
#
# 也就是看最终左右指针会停在哪里。
# 如果我们要找第一个大于等于x的位置，那么我就假设L最终会停在第一个大于等于x的位置，R停在L的左边。
# 这样按照上面那句话，可以把循环不变式描述为“L的左边恒小于x，R的右边恒大于等于x”，这样一来，其他的各种条件就不言自明了。
# 比如循环条件肯定是L小于R，因为我假设R停在L的左边。
# 而L和R转移的时候，根据循环不变式，如果mid小于x，肯定要令L等于mid+1，如果大于等于x，就令R等于mid-1。
#
# 至于初始的时候L和R怎么选，也是看循环不变式，只需要保证初始L和R的选择满足“L的左边恒小于x，R的右边恒大于等于x”，并且不会出现越界的情况即可，
# L必为0，因为0左边可以看作负无穷，恒小于x，R取第一个一定满足条件的（防止mid取到非法值），
# 例如n-1（n开始可以看作正无穷，恒大于等于x，如果保证x在数组里可以选择n-2，其实大于等于n也满足不变式，但是mid可能会取非法值），而且这样一来即使是搜索数组的某一段，也可以很方便根据这个条件地找到初始位置。
# 如果假设L最终会停在第一个大于等于x的位置，R停在L的位置，那么循环不变式就是“L的左边恒小于x，R以及R的右边恒大于等于x”，
# 这样的话，循环条件就是L等于R的时候退出；转移的时候R=mid；初始时，一般取R=n（如果保证x在数组里，也可以取n-1）。
# 其他的情况也类似，比较直观的推导方法就是在要找的位置的分界处（比如在第一个大于等于x的位置后面）画一条线，然后假定L和R最终会停在这条线的左边还是右边，接着倒推各种条件即可。

from typing import List

# []: 返回最小的满足num[i]>=t的idx
def lower_bound(nums: List[int], t: int) -> int:
    l = 0; r = len(nums) - 1;
    while (l <= r):
        m = (l + r) // 2;                    # 对于非负数来说，减法、除法、加法，每一步的结果都不超过 right
        if (nums[m] < t): l = m + 1;        # [m+1, r]
        else: r = m - 1;                    # [l, m-1]
    return l;

# [): 处理左闭右开区间时, r=m, r为看区间
# ps: '(]'一般处理<的
def lower_bound2(nums: List[int], t: int) -> int:
    l = 0; r = len(nums);
    while (l < r):
        m = (l + r) // 2;
        if (nums[m] < t): l = m + 1;    # [m+1,r)
        else: r = m;                     # [l,m)
    return l;   # r

# ():
def lower_bound3(nums: List[int], t: int) -> int:
    l = -1; r = len(nums);
    while (l + 1 < r):      # 区间不为空
        m = (l + r) // 2;
        if (nums[m] < t): l = m;  # (mid, right)
        else: r = m;                # (left, mid)
    return r;

# 处理 ≥,≤,>,< 四种情况
#   >x 等价于 ≥x+1 对于整数来说
#   <x 等价于 (≥x)-1
#   ≤x 等价于 (>x)-1
# 所以都可以用lower_bound()解决
# x+1那个数不一定存在, 不存在时，二分最终得到的是数组长度
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        st = lower_bound(nums, target);
        if (st == len(nums) or nums[st] != target):
            return [-1, -1];
        ed = lower_bound(nums, target + 1) - 1;     # ed是≤x，由于lower_bound()返回的是≥x的数, 因此可以用该函数解决.
        return [st, ed];















