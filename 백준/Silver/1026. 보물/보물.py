n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
B_1 = B

B_1.sort(reverse = True)
A.sort()

mult_list = [A[i] * B_1[i] for i in range(len(A))]
print(sum(mult_list)) 