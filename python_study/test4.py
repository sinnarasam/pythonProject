# prime_list는 1부터 10000사이의 소수가 오름차순으로 저장된 리스트예요.
from prime import prime_list
def generate_prime_list():
    prime_list = []
    for num in range(2, 10001):  # 2부터 10000까지 검사
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(num)
    return prime_list

# print(prime_list)
# 합계가 짝수가 되는 두 소수를 찾는 함수예요.
def goldbach(arr):
    # 합계가 짝수가 되는 두 소수를 작은 수부터 차례로 리스트에 저장해 주세요.
    result = []
    for even in arr:
        for i in range(len(prime_list)):
            if prime_list[i] > even:
                break
            for j in range(i, len(prime_list)):
                if prime_list[i] + prime_list[j] == even:
                    result.append((prime_list[i], prime_list[j]))
                    break
            if len(result) > 0 and result[-1][0] + result[-1][1] == even:
                break

    return result


arr = [int(x) for x in input().split()]

for i in goldbach(arr):
    print(i[0], i[1])