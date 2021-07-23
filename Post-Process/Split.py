import codecs
import re
input_data = codecs.open('.txt', 'r', 'utf-8')
with open(r'.txt','a+',encoding='utf-8') as test:
    test.truncate(0)
for line in input_data.readlines():
    line = (line.rstrip('\n'))
    line = (line.rstrip('\r'))
    A = line
    with open('.txt', 'r') as f:
        word_list = f.read().splitlines()
    start = 0
    index = len(A)
    guessed = False
    f = open('.txt', 'a')
    while index and not guessed:
        if A[start:index] in word_list:
            print(A[start:index],end=' ',file = f)
            start = index
            index = len(A) + 1
        else:
            index += -1
            if index == start:
                index = len(A)
                print(A[start:index], end=' ',file = f)
                guessed = True
    print('',file = f)
writeDir = '.txt'
outfile=open(writeDir,"w")
readDir = '.txt'
f1 = open(readDir,"r")
for line in f1:
    line = (line.rstrip()+'\n')
    line = re.sub(" +", " ", line)
    #if line.find(' ',0) != -1:
    outfile.write(line)
f1.close()
