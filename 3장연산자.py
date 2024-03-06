"""
사칙연산 활용 가능
"""
# page91
print("------사직연산------")
print(1 + 1)
print(3 - 2)
print(5 * 2)
print(6 / 3)

'''
산술연산자
제곱(**), 나머지(%), 몫 구하기(//)
'''
print("-------제곱,나머지,몫구하기-------")
print(2 ** 3)
print(10 % 3)
print(10 // 3)
'''
비교연산자
> , >= , < , <=
'''
print("------비교연산자------")
print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)
'''
비교연산자2
==, !=
'''
print("-----비교연산자2-----")
print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)
print(1 != 3)
'''
단축평가(short circuit evaluation)
'''
print("-----단축평가-----")
print(5 > 4 > 3)
print(4 > 5 > 3)
''''
Quizz. page96
'''
print(5 + 3)
print(6 / 3)
print(5 % 3)
print((5 < 3) or (7 < 3))
''''
3-2.연산자의 우선순위
'''
print("-----연산자의 우선순위-----")
print(2 + 3 * 4)
print((2 + 3) * 4)
'''
3-3.변수로 연산하기
'''
print("-----변수로 연산하기-----")
number = 2 + 3 * 4
print(number)
number = 2 + 3 * 4 + 2
print(number)
number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
'''
복합대입연산자
'''
print("-----복합대입연산자-----")
number = 2 + 3 * 4
print(number)
number += 2
print(number)
''''
Quizz. page105
'''
print("-----Quizz-----")
num = 3
num *= 2
print(num)
'''
Git연동중
'''