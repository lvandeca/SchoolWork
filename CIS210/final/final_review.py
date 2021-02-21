def findLast(s,c):
    counter = 0
    index = -1

    if len(s) == 0:
        return index
    else:
        for char in s:
            if char == c:
                index = counter
            counter += 1
    return index

