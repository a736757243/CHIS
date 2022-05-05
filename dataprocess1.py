#构建训练集
lines = []
f = open("新建文本文档.txt", 'r')  # 原始文件

count = 0
for line in f:
    # 行数计数
    count = count + 1
    lines.append("<question id=" + str(count) + ">	" + line.split(" ")[0] + "的扩展是什么？" + '\n')
    lines.append(
            "<triple id=" + str(count) + ">	" + line.split(" ")[0] + " ||| 扩展 |||" + " ".join(
                line.split(" ")[1:-1]) + '\n')
    lines.append("<answer id=" + str(count) + ">	" + " ".join(
                line.split(" ")[1:-1]) + '\n' + "==================================================" + '\n')
#print(count)
#print(time)
s = ''.join(lines)
f1 = open("WycheproofTrain.txt", 'w')
f1.write(s)
f1.close()
f.close()

# s = ''.join(lines)
# f1 = open("tanin.txt", 'w+')
# f1.write(s)
#f1.close()
del lines[:]