import random
from RSA_Helper import modularExponent, modularInverse, isPrime, miller_rabin, prime_candidate_generator, gcd


def find_primes(number_of_digits):
    """
    Returns a unique pair of primes where both are both prime and are not equal.
    :return: a pair of primes (p, q)
    """
    primes = []
    while len(primes) != 2:
        for n in prime_candidate_generator(number_of_digits, 10000):
            if isPrime(n):
                primes.append(n)
            if len(primes) == 2:
                return tuple(primes)



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
    # Unpack the key into it's components
    key, n = public_key_pair
    # Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [modularExponent(ord(char), key, n) for char in plain_text]
    # Return the array of bytes
    return cipher


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
    # Unpack the key into its components
    key, n = private_key_pair
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr(modularExponent(char, key, n)) for char in cipher_text]

    # Return the array of bytes as a string
    return ''.join(plain)


if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print ("RSA Encrypter/ Decrypter")
    p, q = 2, 3
    primes = []
    for n in prime_candidate_generator(200, 10000000):
        if miller_rabin(n):
            primes.append(n)
        if len(primes) == 2:
            break
    # p = int(raw_input("Enter a prime number (17, 19, 23, etc): "))
    # q = int(raw_input("Enter another prime number (Not one you entered above): "))
    p = primes[0]
    q = primes[1]
    print ("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print ("Your public key has {} digits and your private key has {} digits".format(len(str(public[0])), len(str(private[0]))))
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print('-'.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))