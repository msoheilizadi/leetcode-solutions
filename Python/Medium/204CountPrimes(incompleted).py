def is_prime(number):
    if number <= 1:
        return False
    for i in primes:
        if number % i == 0:
            return False
    return True

n = 10
ans = 0
primes = []

if n==0 or n==1 or n == 2:
    print(ans)

for i in range(3,n,2):
    if is_prime(i):
        ans += 1
print(ans + 1)