#var 1
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = 0
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] == 1:
            not_primes.append(numbers[i])
            break
        elif numbers[i] % numbers[j] == 0 and numbers[i] > numbers[j]:
            is_prime += 1
            continue
        elif numbers[i] > numbers[j]:
            continue
        elif is_prime <= 1:
            primes.append(numbers[i])
            is_prime = 0
            break
        else:
            not_primes.append(numbers[i])
            is_prime = 0
            break
print(primes)
print(not_primes)
#var 2
primes2 = []
not_primes2 = []
is_prime2 = True
for i in range(len(numbers)):
    is_prime2 = True
    if numbers[i] <= 1:
        is_prime2 = False
        not_primes2.append(numbers[i])
        continue
    if numbers[i] == 2:
        is_prime2 = True
        primes2.append(numbers[i])
        continue
    if numbers[i] % 2 == 0:
        is_prime2 = False
        not_primes2.append(numbers[i])
        continue
    for k in range(3, (int(numbers[i] ** 0.5) + 1), 2):
        if numbers[i] % k == 0:
            is_prime2 = False
            break
        else:
            is_prime2 = True
    if is_prime2:
        primes2.append(numbers[i])
    else:
        not_primes2.append(numbers[i])
print(primes2)
print(not_primes2)
