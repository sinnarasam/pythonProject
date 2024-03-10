# 토끼와 거북이가 처음으로 동시에 쉬는 시간을 구해서 출력해 주세요.
N ,M = map(int, input().split())

a, b = N, M
while b != 0 :
    a, b = b, a%b

result = N*M // a

print(result)
