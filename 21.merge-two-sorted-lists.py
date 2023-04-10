#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return

        ans = ListNode()
        head = ans
        while list1 != None and list2 != None:
            val = None
            if list1.val <= list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next

            head.val = val
            head.next = ListNode()
            head = head.next

        while list1 != None:
            head.val = list1.val
            list1 = list1.next
            if list1 != None:
                head.next = ListNode()
                head = head.next

        while list2 != None:
            head.val = list2.val
            list2 = list2.next
            if list2 != None:
                head.next = ListNode()
                head = head.next

        return ans


# @lc code=end
