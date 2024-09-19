numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

is_prime = []
not_prime = []

for i in range(2, 16):
    is_prime_flag = True
    for j in range (2, i):
        if i % j == 0:
            is_prime_flag = False
            break
    if is_prime_flag:
        is_prime.append(i)
    else:
        not_prime.append(i)

print('Primes:', is_prime)
print('Not_primes:', not_prime)


    