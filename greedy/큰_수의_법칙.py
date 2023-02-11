'''
Wirttern by Jack Snider
First written day. : 2023.02.10

-큰 수의 법칙-
난이도 : 하
플이 시간 : 30분
시간 제한 : 1초
메모리 제한 : 128MB
기출 : 2019 국가 교육기관 코딩 테스트

큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여

가장 큰 수를 만드는 법칙이다. 단, 배열 특정한 인덱스( 번호 )에 해당하는 수가 
연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.

예를 들어 순서대로 2,4,5,6으로 이루어진 배열이 있을 때 M이 8이고, K가 3이라고 가정하자.
이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는
6 + 6 + 6 + 5 + 6 + 6 + 6 + 5인 46이 된다.

단, 서로 다른 인덱스에 해당하는 수가 같은 경우에는 서로 다른 것으로 간주한다. 예를 들어 순서대로
3, 4, 3, 4, 3으로 이루어진 배열이 있을 때 M이 7이고, K가 2라고 가정하자. 이 경우 두 번째
원소에 해당하는 4와 네 번째 원소에 해당하는 4를 번갈아 두 번씩 더하는 것이 가능하다. 결과적으로 
4 + 4 + 4 + 4 + 4 + 4 + 4인 28이 도출된다.

-입력조건-
첫 째 줄에 N( 2 <= N <= 1000 ), M( 1 <= M <= 10,000 ), K( 1 <= K <= 10,000 )의 자연수가 주어지며, 각 자연수는 공백으로 구분된다.

둘째 줄에 N개의 자연수가 주어진다, 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1이상 10,000 이하의 수로 주어진다.

입력으로 주어지는 K는 항상 M보다 작거나 같다.

-출력 조건-
첫 째 줄에 Jack Snider의 큰 수의 법칙에 따라 더해진 답을 출력한다.

-입력 예시-
5 8 3
2 4 5 4 6

-출력 예시-
46

'''

# ========================== my try =========================
n,m,k = list( map( int, input().split( ' ' ) ) )

numbers = []
while True:
	numbers = list( map( int, input().split( ' ' ) ) )
	if len( numbers ) == int( n ):
		break
	else:
		print( f'Please input {n} numbers only.' )

sum = 0
tmp = 0
for cnt in range( 0, m ):
	
	tmp_list = list( set( numbers ) )
	tmp_list.sort( reverse = True )
	if tmp < k:
		if numbers.count( tmp_list[ 0 ] ) > 1:
			sum = 1
			sum *= tmp_list[ 0 ] * m
			#print( f'{tmp_list[ 0 ]} * {m} = {sum}')
			break
		sum += tmp_list[ 0 ]
		#print( f'{cnt + 1} : {tmp_list[ 0 ]}' )
		tmp += 1	
	else:
		sum += tmp_list[ 1 ]
		#print( f'{cnt + 1} : {tmp_list[ 1 ]}' )
		tmp = 0
print( sum )

# ===========================================================


# ========================== answer =========================
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map( int, input().split() )
# N개의 수를 공백으로 구분하여 입력받기
data = list( map( int, input().split() ) )


data.sort() # 입력받은 수들 정렬하기
first = data[ n - 1 ] # 가장  큰 수
second = data[ n - 1 ] # 두 번째로 큰 수

result = 0


while True:
	for i in range( k ): # 가장 큰 수를 K번 더하기
		if m == 0: # m이 0이라면 반복문 탈출
			break
		result += first
		m -= 1 # 더할 때마다 1씩 빼기	
	if m == 0: # m이  0이라면 반복문 탈출
		break
	result += second # 두 번째로 큰 수를 한 번 더하기
	m -= 1 # 더 할때마다 1씩 빼기
	
print( result ) # 최종 답안 출력			
	
# ===========================================================

# ========================== answer =========================
# Better wat with Math
# Get input N, M, K by spaces bewteen
n, m ,k = map( int, input().split() ) 
# get N numbers of by spaces between
data = list( map( int, input().split() ) )

data.sort() # sort numbers
first = data[ n - 1 ] # max number
second = data[ n - 2 ] # second max number

# get the count of plus max number
count = int( m / ( k + 1 ))
count += m % ( k + 1 )

result = 0
result += ( count ) * first # adding max number
result += ( m - count ) * second # adding second max number

print( result ) # print final answer

# ===========================================================
