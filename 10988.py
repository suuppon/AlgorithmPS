def CheckPelindrome(word):
    if len(word) == 1:
        return 1
    
    mid = int(len(word)) #mid 번째 char까지 조사한다.

    checkpoint = mid - 1
    
    for i in range(checkpoint):
        if word[i] != word[-i-1]:
            return 0
            

        else:
            pass

        
        if i == checkpoint-1:
            return 1
    


word = input()
print(CheckPelindrome(word))