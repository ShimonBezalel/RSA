"""
An implementation of the RSA algorithm for encrypting & decrypting messages using a public + private key.

Good luck!
"""

import random
from RSA_Helper import modularExponent, modularInverse, isPrime, miller_rabin, prime_candidate_generator, gcd


def find_primes(number_of_digits):
    """
    Returns a unique pair of primes where both are both prime and are not equal.
    :return: a pair of primes (p, q)
    """
    pass


def generate_keypair(p, q):
    """
    Generates two pairs of keys for the RSA algorithm, the public and private keypairs:
        public --  (e, n)
        private --  (d, n)

    p and q are the two large primes for the RSA algorithm. This function calculates n, phi, e, d accordingly.
    :return: a tuple in the format -- ((e, n), (d, n))
    """
    pass


def encrypt(public_key_pair, plain_text):
    """
    Safely encrypts the message in plain_test, char by char.
    Each char is encrypted using the key and n in the provided pair.

    For Example given the message "hey", the function should return:
        [encrypt('h'), encrypt('e'), encrypt('y')]

    :param public_key_pair: a tuple (key, n)
    :param plain_text: The message to encrypt, as string
    :return: A list of each encryption, char by char.
    """
    pass


def decrypt(private_key_pair, cipher_text):
    """
    Decrypts a message in the list cipher_text, block by block.
    Each block has been encrypted using the public keys.
    This reverse function uses the private key to retrieve the char from a block in the list after decrypting.

    For Example given the cipher [1021, 3290, 3289], the function should return:
        decrypt(1021) + decrypt(3290) + decrypt(3289)
    as one long string.

    :param private_key_pair: a tuple (key, n)
    :param cipher_text: The list of blocks to decrypt
    :return: A concatenated string of all the decryptions.
    """
    pass

