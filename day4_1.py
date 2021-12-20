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

    count = 0
    i = 0
    for k in range(0, len(list), ):
        tempList = list[k].split()
        tempList2 = []
       # tempList3 = []

        for n in range(0, len(tempList)):
            tempList2.append((tempList[n], False))

       # tempList3[i].append(tempList2)
        listTables.append([])
        listTables[i].append(tempList2)

        count += 1
        if(count == 5):
            count = 0
            i += 1

    # print(randomNumbers[:10])

    def findWinner():
        for b in randomNumbers:
            for i in range(0, len(listTables)):
                for j in range(0, len(listTables[i])):
                    for c in range(0, len(listTables[i][j])):
                        if(b == listTables[i][j][c][0]):
                            listTables[i][j][c] = (
                                listTables[i][j][c][0], True)

                            # check if the table won
                            hasFalse = False
                            for m in listTables[i][j]:
                                if m[1] == False:
                                    hasFalse = True
                                    break

                            if(not hasFalse):
                                indexWon = j
                                print('found winner:', listTables[j])
                                return indexWon

    print(findWinner())

    # print(listTables[:10])


solution()
