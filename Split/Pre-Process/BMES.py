from math import log
import codecs
import re
from itertools import groupby
# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open("dictionary.txt").read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)
output_data1 = []
def infer_spaces(s):
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k
    return list(reversed(out))
    #return " ".join(reversed(out))
input_data = codecs.open('.txt', 'r', 'utf-8')
output_data = codecs.open('.txt', 'w', 'utf-8')
for line in input_data.readlines():
    #print(line)
    line =(line.rstrip('\n'))
    line = (line.rstrip('\r'))
    line = re.sub(' ','@',line)
    word_list = infer_spaces(line)
    #if word_list[word-1] == ' ' and word_list:
        #output_data.write(word_list + "\tS\n")
    #else:
    for word in range(len(word_list)):
        if len(word_list) == 1:
            output_data.write(word_list[word] + "\tS\n")
        if len(word_list) > 1:
            if word_list[word-1] == '@' and word == len(word_list)-1:
                output_data.write(word_list[word] + "\tS\n")
            if word == 0 and word_list[word+1] == '@':
                output_data.write(word_list[word] + "\tS\n")
            if word == 2 and word_list[word-1] == '@' and word != len(word_list)-1 and word_list[word+1] != '@':
                output_data.write(word_list[word] + "\tB\n")
            if word<len(word_list)-1:
                if word_list[word-1] == '@' and word_list[word+1] == '@':
                    output_data.write(word_list[word] + "\tS\n")
            if word == 0 and word_list[word+1] != '@':
                output_data.write(word_list[word] + "\tB\n")
            if word == (len(word_list)-1) and word_list[word-1] != '@':
                output_data.write(word_list[word] + "\tE\n")
            if 1<word<len(word_list)-2:
                if word_list[word] == '@' and word != 1 and word_list[word+2] == '@' and word_list[word-2] != '@':
                    output_data.write(word_list[word-1] + "\tE\n")
            if word == (len(word_list)-3) and word_list[word+1] == '@' and word_list[word-1] != '@':
                output_data.write(word_list[word] + "\tE\n")
            if word_list[word] == '@' and  word_list[word - 2] == '@' and word != len(word_list)-2 and word_list[word+2] != '@':
                output_data.write(word_list[word + 1] + "\tB\n")
            if 1<word<len(word_list)-2:
                if word_list[word] == '@' and word_list[word - 2] != '@' and word_list[word+2] != '@':
                    output_data.write(word_list[word - 1] + "\tE\n")
                    output_data.write(word_list[word + 1] + "\tB\n")
            if word != 0 and word != (len(word_list)-1) and word_list[word-1] != '@' and word_list[word+1] != '@' and word_list[word] != '@':
                output_data.write(word_list[word] + "\tM\n")
    output_data.write('\n')