
def solution():

    with open("C:\\Users\\Carlv\\Downloads\\input3.txt") as f:
        list = f.readlines()
        f.close()
    start = [0, 0]
    for v in list:
        if v.startswith("f"):
            start[0] += int(v[8])
        if v.startswith("u"):
            start[1] -= int(v[3])
        if v.startswith("d"):
            start[1] += int(v[5])

    print("answer:", start[0]*start[1])


solution()
