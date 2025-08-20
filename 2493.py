from sys import stdin as s
s = open("input.txt", "r")

N = int(s.readline().strip())
nums = list(map(int, s.readline().split()))

stack = []
answer = []
for i, num in enumerate(nums):
    if len(stack) == 0:
        stack.append((num, i))
        answer.append(0)
    elif num >= stack[-1][0]:
        while len(stack) > 0 and num >= stack[-1][0]:
            stack.pop()
        if len(stack) > 0:
            answer.append(stack[-1][1]+1)
        else:
            answer.append(0)
        stack.append((num, i))
    else:
        answer.append(stack[-1][1]+1)
        stack.append((num, i))
    
    # print(stack)

print(' '.join(map(str, answer)))