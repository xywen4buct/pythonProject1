def lines(file):
    for line in file: yield line
    #yield '\n'

f1 = "zhang wen zhang wen"

def block(file):
    block = []
    for line in lines(file):
        print(line)
        if line.strip(): #只要不是空格；
            block.append(line)
        elif block: #如果是空格；
            yield ''.join(block).strip() #输出那些不是空格的拼接单词；
            block = []


for ll in lines(f1):
    print(ll)


#for ff in block(f1):
#    print(ff)