# 题目链接：
#   https://leetcode.cn/problems/reverse-linked-list/
# 题目分析：
#   记录nxt，修改cur，枚举下一个节点（将pre修改成cur，cur更新成nxt）

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None; cur = head;
        while cur: 
            nxt = cur.next;     # 记录nxt
            cur.next = pre;     # 反转
            pre = cur;          # 更新（不要弄反）
            cur = nxt;
        return pre;
    