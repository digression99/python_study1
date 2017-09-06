# 숫자 맞추기 변형 -> 야구게임
# 이미 숫자가 있다면 이미 입력했다고 출력.
# strike, ball 구현 -> S, B -> 모든 X를 S로 바꾸어야 한다.
# 숫자 4개를 한꺼번에 입력받아야 한다

# 6 5 4 7 -> answer
# 4 6 5 7 -> input
# B B B S -> output
# 결국 목표는 맞는 자리의 맞는 숫자를 입력하면 끝나는 게임이다.

# 추가 기능 -> 길이를 늘릴 수 있을까??

import random

n = int(input("enter length(max : 8) :"))

numbers = random.sample(range(1, 9), n)
isCorrect = False
trialLimit = 0

while True:

    str = input("enter {0} number(ex >> 1 2 3 4) : ".format(n))
    answer = [int(x) for x in str.split()]

    if len(answer) != n:
        print("enter again")
        continue

    for i in range(0, n):
        for j in range(0, n):
            if answer[i] == numbers[j] and i == j:
                print("S", end = ' ')
                break
            elif answer[i] == numbers[j] and i != j:
                print("B", end = ' ')
                break
            elif answer[i] != numbers[j] and j == n - 1:
                print("X", end = ' ')
    print()

    trialLimit += 1

    if (answer == numbers):
        print("congrats! you got it!")
        print("tried : {}".format(trialLimit))
        break
    elif trialLimit >= 10:
        print("you spent all you trial")
        print("game over")
        break