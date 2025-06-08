num = 50
ans= 0
pow = 1
while num > 0:
    rem = num%2
    num = num//2
    ans += (rem * pow)
    pow = pow * 10
print(ans)