import sys
input = sys.stdin.readline

while (1):
    s = input().rstrip()
    stack = []
    if s==".":
        break
    else:
        for i in range(len(s)):
            if s[i] in ("(","["):
                stack.append(s[i])
            elif s[i] == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s[i])
                    break
            elif s[i] == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s[i])
                    break

        if not stack and s[-1]==".":
            print("yes")
        else:
            print("no")