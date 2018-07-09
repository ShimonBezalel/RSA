"""
This module provided helping functions for convenience in implementing an RSA encryption algorithm.

Author: Shimon Heimowitz
"""
import random

def prime_candidate_generator(num_of_digits, size):
    BEGIN = 10 ** (num_of_digits)
    R_START = 10 ** (int(num_of_digits * 0.97))
    R_END = 10 ** (int(num_of_digits * 0.98))
    if R_END == R_START:
        R_END = 10 ** (int(num_of_digits + 1))
    candidate = BEGIN
    for _ in range(size):
        candidate += random.randint(R_START, R_END)
        yield candidate


def isPrime(num):
    """
    Test if a number is prime. Makes use of a non-deterministic algorithm -- miller rabin
    :param num: a canditate to check if it is prime
    :return: True if num is prime (May be false negative)
    """
    return miller_rabin(num)


def miller_rabin(n, k=10):
    """
    A  algorithm that quickly asseses if n is prime, within k tries.
    Miller Rabin is a non-deterministic pseudo-prime test

    Raise assertion error when n, k are not positive integers
    or n is 1

    :param n: A candidate which may be prime
    :param k: The number of tries to disqualify n
    :return:    returns True if n is likely a prime, (certainty depends on k)
                returns False if n is definitely not a prime.
    """
    assert n >= 1   # ensure n is bigger than 1
    assert k > 0    # ensure k is a positive integer so everything down here makes sense

    if n == 2:      # quick check for 2
        return True
    if not n & 1:   # quick check for all even numbers, by checking last bit
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in range(k):
        a = random.randint(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True

def gcd(a, b):
    """
    Euclid's algorithm for determining the greatest common divisor
    :return: the greatest common denominator for a and b
    """
    while b != 0:
        a, b = b, a % b
    return a


def modularExponent(a, d, n):
    """
    A fast implementation of an modulo on exponent.
    :return: a ** d (mod n)
    """

    assert d >= 0
    assert n >= 0
    base2D = _int2baseTwo(d)
    base2DLength = len(base2D)
    modArray = []
    result = 1
    for i in range (1, base2DLength + 1):
        if i == 1:
            modArray.append(a % n)
        else:
            modArray.append((modArray[i - 2] ** 2) % n)
    for i in range (0, base2DLength):
        if base2D[i] == 1:
            result *= base2D[i] * modArray[i]
    return result % n

def modularInverse(a, m):
    """
    The modular inverse of n modulo m
    :return: the unique natural number 0 < n0 < m such that n * n0 = 1 mod m.
    """
    g, x, y = _extended_gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def _int2baseTwo(x):
    """
    Convert x to base two as a list of integers
    in reverse order as a list.
    :param x: a positive integer
    :return: a list representing x in binary
    """
    # repeating x >>= 1 and x & 1 will do the trick
    assert x >= 0
    bitInverse = []
    while x != 0:
        bitInverse.append(x & 1)
        x >>= 1
    return bitInverse



def _extended_gcd(a, b):
    """
    Euclid's extended algorithm for determining the greatest common divisor
    :return: a three way tuple with: (gcd, x, y) where x and y are the coefficients for a and b
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = _extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)