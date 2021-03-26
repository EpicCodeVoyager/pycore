
brkt = "((a(b)c)()"
stk = []

for char in brkt:
    if char in ['(']:
        stk.append(char)
    if char in [')']:
        stk.pop()

print(stk)
