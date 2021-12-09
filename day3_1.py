def solution():

    with open("C:\\Users\\Carlv\\Downloads\\input4.txt") as f:
        list = f.readlines()
        f.close()
    lineSize = len(list[1].strip())

    answer = ""
    for i in range(0, lineSize):
        count1 = 0
        count0 = 0
        for v in list:
            if (v[i] == "0"):
                count0 += 1
            if (v[i] == "1"):
                count1 += 1

        if (count1 > count0):
            answer = answer + "1"
        if (count0 > count1):
            answer = answer + "0"

    answer2 = ""

    for k in range(0, len(answer)):
        if(answer[k] == '0'):
            answer2 = answer2 + "1"
        else:
            answer2 = answer2 + "0"

    result = int(answer, 2) * int(answer2, 2)
    print(answer)
    print(int(answer, 2))
    print(answer2)
    print(int(answer2, 2))
    print(result)


solution()
