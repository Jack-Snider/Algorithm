"""
Time mearsurement
파이썬에서는 프로그램 수행 시간과 메모리 사용량을 측정할 수 있다.
알고리즘을 공부하는 과정에서 시간을 측정하는 작업을 굉장히 많이 사용한다.
실질적으로 알고리즘의 소요 시간을 확인해야 자신이 제대로 알고리즘을 
작성하고 있는지 체크할 수 있기 때문이다. 다시 말해 실제 프로그램의 수행
시간을 측정하는 것은 알고리즘의 효율성을 측정하는 가장 기본적인 방법이다.
특정한 프로그램의 수행 시간을 측정하는 소스코드 예시는 다음과 같다.
"""
#=========================================================
import time
start_time = time.time() # 측정 시작

# 프로그램 소스코드

end_time = time.time() # 측정 종료
print( f'time : {end_time - start_time}' ) # 수행 시간 출력
#=========================================================

#=========================================================
"""
수행 시간 측정 소스코드의 형태는 일반적으로 위와 같다. 보통 어떤 알고리즘을 설계한 뒤에
시간 복잡도를 경험적으로 증명하고 싶을 때는 위와 같은 형태의 코드를 자주 이용한다.
예를 들어 '선택 정렬'과 '파이썬의 기본 정렬 라이브러리'의 속도를 비교할 때는 다음과 같이
소스코드를 작성할 수 있다. 선택 정렬을 사용할 때 최악의 경우 시간복잡도가 O(N²)이며, 
파이썬의 기본 정렬 라이브러리는 최악의 경우 시간 복잡도 O(NlogN)을 보장하여 상대적으로
빠르다. 다음 소스코드의 실행 결과가 그러한 성능 차이를 직접적으로 보여준다.
"""
from random import randint

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range( 10000 ):
    array.append( randint( 1,100 ) ) # 1부터 100사이의 랜덤한 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range( len( array ) ):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range( i + 1, len( array ) ):
        if array[ min_index ] > array[ j ]:
            min_index = j
    array[ i ],array[ min_index ] = array[ min_index ], array[ i ] # swap

end_time = time.time() # 측정 종료
print( f'선택 정렬 성능 측정 : {end_time - start_time}' ) # 수행 시간 출력

# 배열을 다시 무작위로 데이터 초기화
array = []
for _ in range( 10000 ):
    array.append( randint( 1,100 ) ) # 1부터 100 사이의 랜덤한 정수

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

end_time = time.time() # 측정 종료

print( f'기본 정렬 라이브러리 성능 측정 : {end_time - start_time}' )