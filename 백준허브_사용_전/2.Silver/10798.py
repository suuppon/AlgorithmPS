input_matrix = list()

length = 0

for _ in range(5):
    row = input()
    new_list = []
    for item in row:
        new_list.append(item)
    input_matrix.append(new_list)
    length += len(new_list)

char = ""

while True:
    for i in range(5):
        if len(input_matrix[i]) != 0:
            char += input_matrix[i].pop(0)
    if len(char) == length:
        break

print(char)