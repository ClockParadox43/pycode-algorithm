# 题目链接：
#   https://leetcode.cn/problems/reverse-nodes-in-k-group/
# 题目分析：
#   每k个节点为一组反转
#   由于不足k个无法反转，所以需要判断链表的长度，在反转之前判断剩余节点个数（>=k无法翻转）
#   每一组翻转的步骤和lc.92是一样的，额外需要做的就是把p0更新成下一段要翻转链表的上一个节点 (p0是哨兵）
#       ps: 其实就是p0.next，注意这里会修改p0的next，所以会先将p0的next存储起来
#           最后更新p0=nxt，开启下一次循环

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0;
        cur = head;
        while cur: n += 1; cur = cur.next;  # 求出链表的长度
        dummy = ListNode(next=head);
        p0 = dummy;

        pre = None;
        cur = p0.next;
        while n >= k:
            n -= k;
            for _ in range(k):  # 反转[l,r]
                nxt = cur.next;
                cur.next = pre;
                pre = cur;
                cur = nxt;
            nxt = p0.next;  # 存储p0的next
            p0.next.next = cur;  # 翻转l和r
            p0.next = pre;
            p0 = nxt;
        return dummy.next;