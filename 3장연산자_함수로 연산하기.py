print('절대값 abs(-5):', abs(-5))
print('제곱한 값 pow(4,2):', pow(4,2))
print('최대값 max(5,12):', max(5,12))
print('최소값 min(5,12):', min(5,12))
print('소수점 이하 첫째 자리에서 반올림한 정수 round(3.14):', round(3.14))
print('소수점 이하 셋째 자리에서 반올림한 값 round(4.6789, 2):', round(4.6789, 2))

from math import *
# math 모듈의 모든 기능을 가져다 쓰겠다 *는 와일드카드 문자로 모든것을 지칭할때 사용

result=floor(4.99)  #내림
print(result)

result2=ceil(3.14)   #올림
print(result2)

result3=sqrt(16)    #제곡근
print(result3)

# math 모듈의 사용법 다른형식
import math

result=math.floor(4.99)  #내림
print(result)

result2=math.ceil(3.14)   #올림
print(result2)

result3=math.sqrt(16)    #제곡근
print(result3)

# random 모듈
from random import *
print(random())
print(random())
print(random())

#0.0이상 10.0미만에서 난수 생성
print(random() *10)
#0.0이상 10.0미만에서 난수 생성 결과를 int() 정수로 변환
print(int(random() *10))
#0.0이상 10.0미만에서 난수 생성 결과를 변환해 1 더함, 즉, 1이상 11미만 정수에서 난수생성
print(int(random() *10)+1)

#random 모듈의 다른 난수 생성 함수들

print(randrange(1,46)) #1이상 46미만
print(randint(1,45))  #1이상 45이하

# 실습문제. 스터디 날짜 정하기
'''
코딩모임 스터디 월 4번, 3번 온라인, 1번 오프라인
조건에 맞는 오프라인 모임 날짜 정하기
1. 날짜를 무작위로 뽑는다.
2. 월별 일수가 다르므로 최소 일수인 28일 이내로 정한다.
3. 매월 1~3일은 스터디를 준비해야 하므로 제외한다.
4. 실행결과 -->> 오프라인 스터디 모임 날짜는 매월 18일로 선정됐습니다.
단, 날짜는 무작위 이므로 책과 결과가 다를 수 있다.
'''
from random import *
date = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정됐습니다.")

'''
연산자를 이용해 온도 단위를 변환하는 프로그램
1. 섭씨 온도를 저장하기 위한 변수 만듦
2. 섭씨 온도를 화씨 온도로 변환하고 새로운 변수에 저장
화씨 온도 = (섭씨 온도 * 9/5)+32
3. 섭씨 온도와 화씨온도를 다음과 같이 출력
섭씨 온도가 30도일때 
섭씨 온도 : 30
화씨 온도 : 86.0

섭씨 온도가 10도 일 때
섭씨 온도 : 10
화씨 온도 : 50.0
'''
celsius = 30
fahrenheit = ( celsius * 9/5) +32
print("섭씨 온도 : " + str(celsius))
print("화씨 온도 : " + str(fahrenheit))


