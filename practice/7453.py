n = int(input())

A, B, C, D = list(), list(), list(), list()

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
C.sort()
D.sort()

C.extend(D)

left = 0
right = 2 * n - 1

cnt = 0

for elt_a in A:
    for elt_b in B:
        summation = elt_a + elt_b
        while left < n and right > n - 1:
            s = C[left] + C[right]
            total = s + summation
            
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                cnt += 1

print(cnt)