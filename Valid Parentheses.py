'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        op="([{"
        clos=")]}"
        dix=dict(zip(clos,op))
        stack=[]
        i=0
        while(i<len(s)):
            if s[i] in op:
                stack.append(s[i])
            else:
                opb=dix[s[i]]
                if len(stack)>0 and stack[-1]==opb:
                    stack.pop()
                else:
                    return 0
            i=i+1
        if len(stack)==0:
            return 1
        return 0
