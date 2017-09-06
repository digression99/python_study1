#
# 뭘 도대체 만들까 생각하다가
# 도무지 떠오르는 게 없어서
# 고전적인 리눅스 식의 게임을 만들어보자
#
# 수도쿠 만들기
#
# 룰 1 -> 가로로 모두 1 ~ 9까지
# 룰 2 -> 세로로 모두 1 ~ 9까지
# 룰 3 -> 작은 사각형 모두 1 ~ 9까지
#python set?
#
import random as rd
import math

interval = 3

def makeMap():
    map = []
    for i in range(0, 9):
        #map.append([0, 1, 2, 3, 4, 5, 6, 7, 8])
        map.append([-1, -1, -1, -1, -1, -1, -1, -1, -1])

    isfin = False
    while not isfin:
        rd.seed()
        for i in rd.sample(range(1, 10), 9):  # 어떤 숫자를
            putOneNum(map, i)

        isfin = True

        for i in range(0, 9):
            for j in range(0, 9):
                if map[i][j] == -1:
                    isfin = False
                    for k in range(0, 9):
                        for l in range(0, 9):
                            map[k][l] = -1

        non = 1

    for i in range(0, 9):
        print(map[i])
    return map

def makeProblem(map):
    numToDelete = 50

    for i in range(0, numToDelete):
        j = rd.randint(0, 8)
        k = rd.randint(0, 8)
        if map[j][k] == -1:
            i -= 1
            continue
        map[j][k] = -1

    return map

def showProblem(map):
    for i in range(0, 9):
        for j in range(0, 9):
            if map[i][j] == -1:
                print('?', end=' ')
            else:
                print(map[i][j], end=' ')
        print()



def putOneNum(map, n):
    for i in rd.sample(range(0, 9), 9):
        for j in rd.sample(range(0, 9), 9):
            if boxCheck(map, i, j, n) and lineCheck(map, i, j, n):
                if map[i][j] == -1:
                    map[i][j] = n

def lineCheck(map, i, j, n):
    for k in range(0, 9):
        if n == map[k][j]:
            return False
    for k in range(0, 9):
        if n == map[i][k]:
            return False
    return True


def boxCheck(map, i, j, num): # 하나의 박스 안에 숫자가 안 겹치면 true
    box = []
    boxi = math.floor(i / 3) * 3
    boxj = math.floor(j / 3) * 3

    for k in range(0, 3):
        box += map[boxi + k][boxj:boxj + 3]

    for i in range(0, 9):
        if box[i] == num:
            return False
    return True

m = makeMap()
makeProblem(m)
showProblem(m)
# 지금 문제 로직에서는 답이 두개다. 이걸 어떻게 해결할까.





