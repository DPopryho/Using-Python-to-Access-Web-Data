import re


def file(txtfile):
    newlst = list()
    for line in txtfile:
        line = line.rstrip( )
        num = re.findall('([0-9]+)', line)
        if len(num) < 1: continue
        for i in num:
            i = int(i)
            newlst.append(i)

    return sum(newlst)

handl = open('database.txt')

print(file(handl))
