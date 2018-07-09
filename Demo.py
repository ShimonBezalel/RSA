from Primes import gen_candidates, miller_rabin
from RSA_Solution import generate_keypair, encrypt, decrypt

if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print ("RSA Encrypter/ Decrypter")
    p, q = 2, 3
    primes = []
    for n in gen_candidates(200, 10000000):
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
    print ("Your public key is {} and your private key is {}".format(public, private))
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))