def is_prime(n):
    """주어진 숫자 n이 소수인지 확인합니다."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def goldbach_conjecture(even_number):
    """골드바흐의 추측을 사용하여 주어진 짝수를 두 소수의 합으로 표현합니다."""
    for num in range(2, even_number):
        if is_prime(num) and is_prime(even_number - num):
            return num, even_number - num
    return None, None

def print_goldbach_numbers(max_value):
    """1부터 주어진 최대값까지의 모든 짝수에 대해 골드바흐의 추측을 검증하고 결과를 출력합니다."""
    for even_number in range(4, max_value + 1, 2):
        prime1, prime2 = goldbach_conjecture(even_number)
        if prime1 and prime2:
            print(f"{even_number} = {prime1} + {prime2}")

# 사용자 입력값 예시: 20
max_value = int(input("최대값을 입력하세요: "))
print_goldbach_numbers(max_value)
