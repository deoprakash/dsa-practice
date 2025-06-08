num = 110010
ans = 0
pow = 1
while num > 0:
    rem = num%10
    num = num//10
    ans += (rem * pow)
    pow = pow * 2
print(ans)

