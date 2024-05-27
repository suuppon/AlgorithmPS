k, q, l, b, kn, p = map(int, input().split())

true_k = 1
true_q = 1
true_l = 2
true_b = 2
true_kn = 2
true_p = 8

kd = true_k - k
qd = true_q - q
ld = true_l - l
bd = true_b - b
knd = true_kn - kn
pd = true_p - p

print("{} {} {} {} {} {}".format(kd, qd, ld, bd, knd, pd))