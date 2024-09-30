#!/usr/bin/python3
def sieve_of_eratosthenes(n):
    """ Returns a list of primes up to n """
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

        p += 1
    return [i for i in range(2, n + 1) if is_prime[i]]


def isWinner(x, nums):
    """ Determines the winner after x rounds of the Prime Game """
    if x <= 0 or not nums:
        return None

    max_num = max(nums)

    primes = sieve_of_eratosthenes(max_num)

    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if i in primes else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
