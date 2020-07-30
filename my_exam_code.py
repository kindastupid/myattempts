a = b = 0
p = 35
k351ch = k352ch = nek35ch = 0
k351nech = k352nech = nek35nech = 0
n = int(input())
for i in range(n):
    x = int(input())
    if x % p == 0 and x %2 == 0:
        if x > k351ch:
            k352ch = k351ch
            k351ch = x
        elif x > k352ch:
            k352ch = x
    if x % p == 0 and x %2 != 0:
        if x > k351nech:
            k352nech = k351nech
            k351nech = x
        elif x > k352ch:
            k352nech = x
    if x % p != 0 and x %2 == 0:
        if x > nek35ch:
            nek35ch = x
    if x%p !=0 and x%2 != 0:
        if x > nek35nech:
            nek35nech = x
if k352ch > nek35ch:
    a = k352ch
else:
    a = nek35ch
if k352nech > nek35nech:
    b = k352nech
else:
    b = nek35nech
if a + k351ch > b + k351nech:
    print(a, k351ch)
else:
    print(b, k351nech)
