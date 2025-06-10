from sys import stdin as s
s = open("input.txt", "r")

strings = s.readline().strip()

PRIORITY = {
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
    '(': 0,
    ')': 0
}

answer = ''
oper_stack = []
for str in strings:
    # print(str, oper_stack)
    if str.isalpha():
        answer += str
    elif str == '(':
        oper_stack.append(str)
    elif str == ')':
        while True:
            oper = oper_stack.pop()
            if oper == '(': break
            answer += oper
    else:
        while oper_stack:
            if PRIORITY[str] <= PRIORITY[oper_stack[-1]]:
                answer += oper_stack.pop()
            else:
                break
        
        oper_stack.append(str)

while oper_stack:
    answer += oper_stack.pop()

answer