"""
복잡도는 알고리즘의 성능을 나타내는 척도이다.
복잡도는 시간 복잡도( Time Complecity )와 공간 복잡도( Space Complexity )
로 나눌 수 있다. 쉽게 말하면 시간 복잡도는 특정한 크기의 입력에 대하여 알고리즘이
얼마나 오래 걸리는지를 의미하고, 공간 복잡도는 특정한 크기의 입력에 대하여 알고리즘이
얼마나 많은 메모리를 차지하는지를 의마한다.

Summary
시간 복잡도 : 알고리즘을 위해 필요한 연산의 횟수
공간 복잡도 : 알고리즘을 위해 필요한 메모리의 양


"""


# 시간 복잡도( Time Complexity )
"""
시간 복잡도를 표현할 때는 빅오( Big-O )표기법을 사용한다. 엄밀한 정의는 아니지만,
빅오 표기법을 간단히 정의하자면 가장 빠르게 증가하는 항만을 고려하는 표기법이다.
다시 말해 함수의 상한만을 나타낸다. 
"""
#=========================================================
array = [ 3, 5, 1, 2, 4 ]   # 5개의 데이터( N = 5 )
summary = 0                 # 합계를 저장할 변수

# 모든 데이터를 하나씩 확인하며 합계를 계산
for x in array:
    summary += x

# 결과를 출력
print( summary ) # O(N) : N번의 연산을 수행 [ 선형 시간 ]
#=========================================================

#=========================================================
a = 5
b = 7
print( a + b ) # O(1) : 1번의 연산을 수행 [ 상수 시간 ]
#=========================================================


#=========================================================
array = [ 3, 5, 1, 2, 4 ]   # 5개의 데이터( N = 5 )

for i in array:
    for j in array:
        temp = i * j
        print( temp ) # O(N²)
"""
2중 반복문이라서 N x N만큼의 연산이 필요하다는 것을 유추할 수 있다.
하지만 모든 2중 반복문의 시간복잡도가 O(N²)은 아니다. 만약 소스코드가 내부적으로
다른 함수를 호출한다면 내부 함수의 시간 복잡도까지 고려해야 한다.
"""
#=========================================================

#=========================================================
"""
빅오 표기법             명칭
O(1)                    상수 시간( Constant time )
O(logN)                 로그 시간( Log time )
O(N)                    선형 시간
O(NlogN)                로그 선형 시간
O(N²)                   이차 시간
O(N³)                   삼차 시간
O(2ⁿ)                   지수 시간
"""
#=========================================================

print( 29 + 34 ) # O(1)



