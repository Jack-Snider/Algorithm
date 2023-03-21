'''
실전 문제

게임 개발
난이도 ●●○ | 풀이 시간 40분 | 시간 제한 1초 | 메모리 제한 128MB

현민이는 게임 캐릭터가 맵 안에서 움직이는 시스템을 개발 중이다. 캐릭터가 있는 장소는 1 X 1 크기의
정사각형으로 이뤄진 N X M 크기의 정사각형으로, 각각의 칸은 육지 또는 바다이다. 캐릭터는 동서남북 중
한 곳을 바라본다.

맵의 각 칸은 ( A,B )로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 
개수이다. 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다. 캐릭터의 움직임을
설정하기 위해 정해 놓은 메뉴얼은 이러하다.

1.  현재 위치에서 현재 방향을 기준으로 왼쪽 방향( 반시계 방향으로 90도 회전환 방향 )부터 차례대로 갈 곳을 정한다.

2.  캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.

3.  만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로
    돌아간다. 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

현민이는 위 과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트하려고 한다.
메뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.

- 입력 조건 -
1.  첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. ( 3 <= N,M <= 50 )
2.  둘째 줄에 게임 캐릭터가 있는 칸의 좌표 ( A,B )와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다.
    방향 d의 값으로는 다음과 같이 4가지가 존재한다.
    - 0 : 북쪽
    - 1 : 동쪽
    - 2 : 남쪽
    - 3 : 서쪽

3.  셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로,
    각 죽의 데이터는 동쪽 순서대로 주어진다. 맵의 외곽은 항상 바다로 되어 있다.
    - 0 : 육지
    - 1 : 바다

4.  처음에 캐릭터가 위치한 칸의 상태는 항상 육지이다.
5.  첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.

- 입력 예시 -
4 4         # 4 X 4 맵 생성
1 1 0       # ( 1,1 )에 북쪽( 0 )을 바라보고 서 있는 캐릭터
1 1 1 1     # 첫 줄은 모두 바다
1 0 0 1     # 둘째 줄은 바다/육지/육지/바다
1 1 0 1     # 셋째 줄은 바다/바다/육지/바다
1 1 1 1     # 넷째 줄은 모두 바다

- 출력 예시 -
3

'''
# ========================== my try =========================
def move( direction , location ): # function for every move
	
	# return type : list
	# return [ x,y,facing direction ] -> x,y are location
	
	dx = location[ 0 ] # x
	dy = location[ 1 ] # y
	
	# parameter direction should be in range 0 ~ 3
	if int( direction ) not in( 0,3 + 1 ):
		return '[ WARNING ] : direction must be in range 0 ~ 3'
	
	
	# parameter location should be list type with length 2 only
	if len( location ) != 2:
		return '[ WARNING ] : length of location must be 2 only'
		
	# begins
	if direction == '0': # North
		# y : -1
		dy -= 1
		return list( ( dx,dy ) )
	elif direction == '1': # East
		# x : +1
		dx += 1
		return list( ( dx,dy ) )
	elif direction == '2': # South
		# y : +1
		dy += 1
		return list( ( dx,dy ) )
	elif direction == '3': # West
		# x : -1
		dx -= 1
		return list( ( dx,dy ) )
	else:
		return '[ WARNING ] : Direction parameter'


def sea_check( next_step, game_map ):
	# check if the next step to go is sea or not
	# parameter next_step must be list or tuple like ( x, y )
	# parameter game_map is the map of this game
	
	# retyrn type is bool
	# if sea, True. if not, False.
	
	if len( next_step ) == 2:
		next_step_x = next_step[ 0 ]
		next_step_y = next_step[ 1 ]
		if game_map[ next_step_x ][next_step_y ] == 1:
			return True # if sea
		else:
			return False # if not sea
			
	return True # default is True
			
		
	
def went_already( next_step, game_map ):
	# check if you already have been  to the location you are about to go
	# in this function, save every location you have been to
	
	# parameter next_step is the location you are about to go ( type - list )
	# parameter game_map is the map of this game ( type - 2D list )
	
	# return type is bool
	
	# if you have been already, True. if you haven't been yet, False.
	
	# You have to save every move made
	
	if len( next_step ) == 2:
		next_step_x = next_step[ 0 ]
		next_step_y = next_step[ 1 ]
		
		# Check if the next_step_x and next_step_y are in the range of game_map 
	
	
	
def movable( is_sea, has_been ):
	
	# is_sea = sea_check( nexts_step, game_map )
	# has_been = went_already( next_step, game_map )
	
	# return type is bool
	# if the next_step is movable, True. if not, False 
	pass
	
n,m = input().split() # variables for current location
dx,dy,direction = input().split() # for facing direction

game_map = [ [ 0 ] * int( n ) for _ in range( int( m ) ) ] # create 2D list of game map

print( game_map )
print( len(game_map[0]))

# ===========================================================

# ========================== answer =========================
# ===========================================================
