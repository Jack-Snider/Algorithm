'''
예제 4-1 상하좌우
난이도 ●○○ | 풀이시간 15분 | 시간 제한 1초 | 메모리 제한 128MB

여행가 A는 N x N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 x 1 크기의 정사각형으로 나
누어져 있다. 가장 왼쪽 위 좌표는 ( 1, 1 )이며, 가장 오른쪽 아래 좌표는 ( N, N )에 해당한다. 
여행가 A는 상,하,좌,우 방향으로 이동할 수 있으며, 시작 좌표는 항상 ( 1, 1 )이다. 
우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여있다.

계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L,R,U,D 중 하나의 문자가 반복적으로 적혀있다.
각 문자의 의미는 다음과 같다.

L : 왼쪽으로 한 칸 이동
R : 오른쪽으로 한 칸 이동
U : 위로 한 칸 이동
D : 아래로 한 칸 이동

이때 여행가 A가 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다. 예를 들어 ( 1, 1 )의 위치에서
L혹은 U를 만나면 무시된다.  예를들어 N = 5인 지도와 R,R,R,U,D,D의 계획서가 있을 때
여행가가 움직이게 되는 위치는 순서대로  ( 1,2 ), ( 1,3 ), ( 1,4 ), ( 1,4 ), ( 2,4 ), ( 3,4 )이므로
최종적으로 여행가 A가 도착하데 되는 곳의 좌표는 ( 3,4 )이다. 다시 말해 3행 4열의 위치에 해당하므로
( 3,4 )라고 적는다. 계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을
작성하시오.

입력조건 
    1). 첫째 줄에 공간의 크기를 나타내는 N이 주어진다( 1 <= N <= 100 )
    2). 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. ( 1 <= 이동 횟수 <= 100 )

출력조건
    1). 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 ( X,Y )를 공백으로 구분하여 출력한다.

입력예시 
5
R R R U D D

출력예시
3 4

'''
# ========================== my try =========================
n = int( input() )
userMap = input().split()
x,y = 1,1
for moveType in userMap:

    if moveType == 'L':
        # L : y - 1
        if y == 1:
            #print( f'moveType : {moveType} = {x},{y}')
            continue
        else:
            y -= 1
            print( f'moveType : {moveType} = {x},{y}')
    elif moveType == 'R':
        # R : y + 1
        if y == n:
            #print( f'moveType : {moveType} = {x},{y}')
            continue
        else:
            y += 1
            print( f'moveType : {moveType} = {x},{y}')
    elif moveType == 'U':
        # U : x - 1
        if x == 1:
            #print( f'moveType : {moveType} = {x},{y}')
            continue
        else:
            x -= 1
            print( f'moveType : {moveType} = {x},{y}')
    elif moveType == 'D':
        # D : x + 1
        if x == n:
            #print( f'moveType : {moveType} = {x},{y}')
            continue
        else:
            x += 1
            print( f'moveType : {moveType} = {x},{y}')

print( f'{x} {y}')
    

# ===========================================================