'''
Lab 10, Question 2. Numbering words in a file.
'''
# imports file
def wordList():
    file = input("Enter text file you wish to import")
    with open(file) as f:
        return f.readlines()

def main():
    myWordList = wordList()
    for num in range(len(myWordList)):
        print(num , '\t', myWordList[num])
main()