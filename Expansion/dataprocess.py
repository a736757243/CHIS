#构建训练集
lines = []
f = open("Oracle1.txt", 'r')  # 原始文件

count = 0
for line in f:
    # 行数计数
    count = count + 1
    if (count % 3 == 1):
        lines.append("<question id=" + str((count // 3) + 1) + ">	" + line.strip('\n') + "的扩展是什么？" + '\n')
    elif (count % 3 == 2):
        lines.append(
            "<triple id=" + str((count // 3) + 1) + ">	" + line.split(" ")[0] + " ||| 扩展 ||| " + " ".join(
                line.split(" ")[1:-1]) + '\n')
    elif (count % 3 == 0):
        lines.append("<answer id=" + str((count // 3)) + ">	" + line.strip(
            '\n') + '\n' + "==================================================" + '\n')
#print(count)
#print(time)
s = ''.join(lines)
f1 = open("train.txt", 'w+')
f1.write(s)
f1.close()
f.close()

# s = ''.join(lines)
# f1 = open("tanin.txt", 'w+')
# f1.write(s)
#f1.close()
del lines[:]