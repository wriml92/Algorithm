H, M = map(int, input().split())

if M >= 45:
    print(H, M - 45)
else:
    M += 15
    if H == 0:
        H = 23
    else:
        H -= 1
    print(H, M)