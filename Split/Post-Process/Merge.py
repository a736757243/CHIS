import codecs
def clone_runoob(li1):
    li_copy = li1[:]
    return li_copy
input_data = codecs.open('.txt', 'r', 'utf-8')
output_data = codecs.open('.txt', 'w', 'utf-8')
with open('.txt','r') as f:
    word_list = f.read().splitlines()
    #word_list = (word_list.rstrip('\n'))
    #print(word_list)
suffix_list = ['s','es','r','ed','er','ly','ing','able']
prefix_list = ['un','pre','re','per','sub']
for line in input_data.readlines():
    line = (line.strip('\r\n'))
    li1 = line.split(" ")
    A = li1
    #print(A)
    if len(A) > 1:
        for i in range(len(A) - 1):
            # B = ['ly', 'num', 'char','sets']
            # A = ['ly', 'num', 'char','sets']
            # print(A[0])
            value = A[i:i + 2]
            str = ''.join(value)
            str1 = ''.join(A[i + 1])
            str2 = ''.join(A[i + 1:i + 3])
            str0 = ''.join(A[i])
            #print(str)
            C = clone_runoob(A)
            C[i] = str
            C.pop(i + 1)
            if str in word_list:
                output_data.write(' '.join(C) + '\n')
                break
            if str not in word_list and str1 in suffix_list:
                output_data.write(' '.join(C) + '\n')
                break
            if str not in word_list and i == (len(A) - 2) and str1 not in suffix_list and str0 not in prefix_list:
                output_data.write(' '.join(A) + '\n')
                break
            if str not in word_list and str0 in prefix_list:
                output_data.write(' '.join(C) + '\n')
                break
    else:
        output_data.write(' '.join(A) + '\n')
output_data.write(' ')
