#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        matches = {"(": ")", "{": "}", "[": "]"}
        q = list()
        for char in s:
            if char in "({[":
                q.append(char)
            else:
                if len(q) == 0:
                    return False
                else:
                    last = q.pop()
                    if matches.get(last, False) != char:
                        return False
        if len(q) == 0:
            return True
        else:
            return False


# @lc code=end
