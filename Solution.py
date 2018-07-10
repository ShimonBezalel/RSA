import random
from RSA_Helper import modularExponent, modularInverse, isPrime, miller_rabin, prime_candidate_generator, gcd


def generate_keypair(p, q):
    """
    Generates two pairs of keys for the RSA algorithm, the public and private keypairs:
        public --  (e, n)
        private --  (d, n)

    p and q are the two large primes for the RSA algorithm. This function calculates n, phi, e, d accordingly.
    :return: a tuple in the format -- ((e, n), (d, n))
    """
    if not (isPrime(p) and isPrime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    # n = pq
    n = p * q

    # Phi is the totient of n
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are coprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = modularInverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))