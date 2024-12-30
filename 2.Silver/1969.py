from collections import Counter

n, m = map(int, input().split())

dna_list = []

for _ in range(n):
    dna = input()
    dna_list.append(dna)

total_hamming_distance = 0
result = ''

for i in range(m):
    dna_col = [dna[i] for dna in dna_list]
    c = Counter(dna_col).most_common()
    c.sort(key=lambda x: (-x[1], x[0]))
    mode = c[0][0]
    result += mode[0][0].capitalize()
    total_hamming_distance += sum(1 for dna in dna_list if dna[i] != mode)
    
    
print(result)
print(total_hamming_distance)