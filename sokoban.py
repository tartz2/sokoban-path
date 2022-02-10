import sys

f = open(sys.argv[1], "r")
rows = f.readlines()

rowCount = 0
colCount = 0

graph = []
postmp = [-1,-1,-1,-1]


#Taking the input and putting it into a 2d array
for row in rows:
    tmp = row.split("\n")
    tmp2 = tmp[0]
    tmp3 = tmp2.split(",")
    numCount = 0
    for num in tmp3:
        if int(num) == 2:
            postmp[0] = numCount
            postmp[1] = rowCount
            numCount += 1
        elif int(num) == 3:
            postmp[2] = numCount
            postmp[3] = rowCount
        numCount += 1
    graph.append(tmp3)
    rowCount += 1
    colCount = numCount;

tupPos = tuple(postmp)
states = set()

def getNeighbors(tmp, neighbor, states):
    px = tmp[0]
    py = tmp[1]
    bx = tmp[2]
    by = tmp[3]

    #get up neighbor
    if py > 0:
        if graph[py - 1][px] != '1':
            if px == bx:
                if by > 0:
                    if graph[by - 1][bx] != '1':
                        newState = (px, py-1, bx, by-1)
                        if newState not in states:
                            neighbor.append(newState)
            else:
                newState = (px, py - 1, bx, by)
                if newState not in states:
                    neighbor.append(newState)

    # get left neighbor
    if px > 0:
        if graph[py][px - 1] != '1':
            if py == by:
                if bx > 0:
                    if graph[by][bx - 1] != '1':
                        newState = (px - 1, py, bx - 1, by)
                        if newState not in states:
                            neighbor.append(newState)
            else:
                newState = (px - 1, py, bx, by)
                if newState not in states:
                    neighbor.append(newState)

    # get down neighbor
    if py < rowCount - 1:
        if graph[py + 1][px] != '1':
            if px == bx:
                if by < rowCount - 1:
                    if graph[by + 1][bx] != '1':
                        newState = (px, py + 1, bx, by + 1)
                        if newState not in states:
                            neighbor.append(newState)
            else:
                newState = (px, py + 1, bx, by)
                if newState not in states:
                    neighbor.append(newState)
    # get right neighbor
    if px < colCount - 1:
        if graph[py][px + 1] != '1':
            if py == by:
                if bx < colCount - 1:
                    if graph[by][bx + 1] != '1':
                        newState = (px + 1, py, bx + 1, by)
                        if newState not in states:
                            neighbor.append(newState)
            else:
                newState = (px + 1, py, bx, by)
                if newState not in states:
                    neighbor.append(newState)

def search(tmp, graph, states):
    neighbors = []
    getNeighbors(tmp, neighbors, states)
    while len(neighbors) > 0:
        #print(neighbors)
        curState = neighbors.pop()
        if graph[curState[3]][curState[2]] == '4':
            print("YES")
            quit()
        states.add(curState)
        getNeighbors(curState, neighbors, states)
    return

search(tupPos, graph, states)

print("NO")

