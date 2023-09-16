class Solution:
    def isValid(self, s: str) -> bool:
        list_stack = []
        for ch in s:
            if ch in ['(', '[', '{']:
                list_stack.append(ch)
            else:
                if ch == ')':
                    if len(list_stack) > 0:
                        if list_stack[-1] == '(':
                            list_stack.pop(-1)
                        else:
                            return False
                    else:
                        return False
                elif ch == ']':
                    if len(list_stack) > 0:
                        if list_stack[-1] == '[':
                            list_stack.pop(-1)
                        else:
                            return False
                    else:
                        return False
                elif ch == '}':
                    if len(list_stack) > 0:
                        if list_stack[-1] == '{':
                            list_stack.pop(-1)
                        else:
                            return False
                    else:
                        return False
        return True if len(list_stack) == 0 else False


obj = Solution()
print("(()[)]{}", obj.isValid("(()[)]{}"))
print("()", obj.isValid("()"))
print("()[]{}", obj.isValid("()[]{}"))
print("(]", obj.isValid("(]"))
print(obj.isValid("["))
print("]", obj.isValid("]"))
print("{[]}", obj.isValid("{[]}"))
print("[", obj.isValid(""))

"""
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
"""