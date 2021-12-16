def solution():
    with open("C:\\Users\\Carlv\\Downloads\\input4.txt") as f:
        list = f.readlines()
        f.close()
    lineSize = len(list[1].strip())

    list_copy = list.copy()  # make a copy for the second fucntion below

    def recursiveOxy(listR, j):
        count1 = 0
        count0 = 0
        listNew = []  # new list with values that should stay
        for v in listR:
            if (v[j] == "0"):
                count0 += 1
            if (v[j] == "1"):
                count1 += 1

        if(count1 >= count0):
            for v in listR:
                if(v[j] == '1'):
                    listNew.append(v)
        else:
            for v in listR:
                if(v[j] == '0'):
                    listNew.append(v)

        if(len(listNew) == 1):
            return int(listNew[0], 2)
        else:
            j = j+1
            return recursiveOxy(listNew, j)

    def recursiveCo2(listR, j):
        count1 = 0
        count0 = 0
        listNew = []
        for v in listR:
            if (v[j] == '0'):
                count0 += 1
            if (v[j] == '1'):
                count1 += 1

        if(count1 >= count0):
            for v in listR:
                if(v[j] == '0'):
                    listNew.append(v)
        else:
            for v in listR:
                if(v[j] == '1'):
                    listNew.append(v)

        if(len(listNew) == 1):
            return int(listNew[0], 2)
        else:
            j = j+1
            return recursiveCo2(listNew, j)

    return(recursiveCo2(list, 0) * recursiveOxy(list_copy, 0))


print(solution())
