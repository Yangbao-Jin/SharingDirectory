from itertools import combinations

T = input("")
data = []

for i in range(int(T)):
    user_input = input("")
    data.append(user_input)

def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in data:
    good_sums = []
    possible_primes = []
    for j in range(2, int(i) * 2):
        if is_prime(j):
            possible_primes.append(int(j))

    possible_additives = [list(x) for x in combinations(possible_primes, 2)]

    for s in possible_additives:
        if (s[0] + s[1])/2 == int(i):
            good_sums.append([s[0], s[1]])

    print(f'{good_sums[0][0]} {good_sums[0][1]}')