line = []
line1 = []
f = open("toExpansion1.txt","r")
f1 = open("abbreviation.txt","r")
lines = f1.readlines()
for line in lines:
    line1.append(line.strip('\n'))
print(line1)
i = 0
for line in f:
    # while i < line.count(' '):
    for i in range(line.strip().count(' ') + 1):
        if line.strip().split(' ')[i] in line1:
            print(line.strip().split(' ')[i])
            # i = i + 1


# fobj=open('1.txt','w+')
# with open('toExpansion1.txt','r') as f:
#      for line in f:
#           with open('abbreviation.txt','r') as obj:
#                   for strs in obj.readlines():
#                          if line.strip() in strs.strip():
#                               fobj.write(strs.strip()+"\n")
# fobj.close()