'''
Lab 10, Quesion 2. 
'''
# CALCULATE AVERAGE LENGTH OF WORD IN FILE
# imports file
def wordList():
    file = input('Enter the file you wish to import. ')
    with open(file) as f:
        return f.readlines()

# length of the words in file
def wordAverage(myWordList, length, num):
    for word in myWordList:
        length += len(word)
    cal = length / num
    return cal

def main():
    length = 0
    myWordList = wordList()
    num = len(myWordList)
    ans = wordAverage(myWordList, length, num)
    print(ans)



main()











