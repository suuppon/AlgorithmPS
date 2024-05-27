class GroupWordChecker:
    def __init__(self, word):
        self.word = word
    
    def Checker(word):
        n = len(word)

        for i in range(n):

            if i == n-1:
                return 1
            
            if word[i] == word[i+1]:
                pass
            else:
                if word[i] in word[i+1:]:
                    return 0
                else:
                    pass

    def main():
        n = int(input())
        c = 0
        for _ in range(n):
            word = input()
            c += GroupWordChecker.Checker(word)

        print(c)


if __name__ == "__main__":
    GroupWordChecker.main()