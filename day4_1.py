def solution():
    with open("C:\\Users\\Carlv\\Downloads\\input41.txt") as f:
        randomNumbers = f.readline().strip().split(
            ',')  # get the numbers announced in bingo
        list = []
        for line in f:
            if line.rstrip():
                # get all non empty lines from file into a list
                list.append(line)
        f.close()

    listTables = []

    # save all tables as lists of tuples with a value and a Boolean to mark
    # if it was already announced or not, and then save those lists nested in
    # listTables
    for k in range(0, len(list), ):
        tempList = list[k].split()
        tempList2 = []
        for n in range(0, len(tempList)):
            tempList2.append((tempList[n], False))

        listTables.append(tempList2)

    # print(randomNumbers[:10])

    def findWinner():
        for b in randomNumbers:
            for i in range(0, len(listTables)):
                for j in range(0, len(listTables[i])):
                    if(b == listTables[i][j][0]):
                        listTables[i][j] = (listTables[i][j][0], True)

                        # check if the table won
                        for j in listTables[i]:
                            if False in j:
                                continue
                            else:
                                indexWon = i
                                return indexWon

    print(findWinner())

    # print(listTables[:10])


solution()
