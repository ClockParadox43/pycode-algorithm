# 题目链接：
#   https://leetcode.cn/problems/reverse-linked-list-ii/
# 题目分析：
#   反转[l,r]这段链表
#   注意区间前面可能没有节点存在，所以还需要再表头添加一个哨兵节点

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p0 = dummy = ListNode(next = head);
        for _ in range(left - 1): p0 = p0.next;           # 从dummy出发循环left-1次，最终到区间l的上一个节点
        # 反转[l,r]
        pre = None; cur = p0.next;
        for _ in range(right - left + 1):
            nxt = cur.next;
            cur.next = pre;
            pre = cur;
            cur = nxt;
        # 反转l和r
        p0.next.next = cur; p0.next = pre;
        return dummy.next;