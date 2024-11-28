#Find the Count of Prime Numbers
def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def countPrimes(nums: list) -> int:
    return sum(1 for num in nums if isPrime(num))
