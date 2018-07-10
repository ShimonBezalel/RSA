from RSA import generate_keypair, encrypt, decrypt, find_primes

if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print ("RSA Encrypter/ Decrypter")
    p, q = find_primes(200)
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