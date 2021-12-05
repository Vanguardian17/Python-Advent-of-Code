def solution5():

    with open("C:\\Users\\Carlv\\Downloads\\input4.txt") as f:
        list = f.readlines()
        f.close()
    lineSize = len(list[1].strip())

    answer = []
    for i in range(0, lineSize-1):
        count1 = 0
        count0 = 0
        for v in list:
            if (v[i] == "0"):
                count0 += 1
            if (v[i] == "1"):
                count1 += 1

        print(count1, count0)
        if (count1 > count0):
            answer.append(1)
        if (count0 > count1):
            answer.append(0)
    print(answer)

    answer2 = []

    for k in answer:
        if(k == 0):
            answer2.append(1)
        else:
            answer2.append(0)
    print(answer2)


solution5()
