def decimal_to_binary(decimal_num):
    binary_result = ""

    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_result = str(remainder) + binary_result
        decimal_num //= 2

    if binary_result == "":
        binary_result = "0"

    return binary_result
List = []
decimal_num = int(input())
binary_num = decimal_to_binary(decimal_num)

for i in range(len(str(binary_num))):
    List.append(int(str(binary_num)[i]))
print(sum(List))