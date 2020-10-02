import hashlib
import base64
import random

class auth:
    def __init__(self):
        self.code_verifier = ''
        self.hash_verifier = ''
        self.base64_verifier = ''

    # Generates a cryptographically random string between 43 adn 128 characters in length. Containing letters, digits, underscores, periods, hyphens, or tildes.
    # Returns the string generated
    def generate_code_verifier(self):
        crypto_random_string = 'abcdefghijklmnopqrstuvwxyz1234567890_.-~'

        lower_bound = 43
        upper_bound = 128
        code_verifier_len = random.randint(lower_bound, upper_bound)

        code_verifier = ''.join(random.choice(crypto_random_string) for _ in range(code_verifier_len))
        return code_verifier

    # Hashes a given string using the SHA256 algorithm
    # Returns the hashed string
    def generate_hash_verifier(self,code_verifier_string):
        return hashlib.sha256(code_verifier_string.encode('utf-8')).hexdigest()

    # Base 64 encodes a given string
    # Returns encoded string
    def generate_base64_verifier(self, hash_verifier_string):
        return base64.standard_b64encode(hash_verifier_string)

def main():
    #print(read_client_credentials(client_credentials_file))
    au = auth()

    au.code_verifier = au.generate_code_verifier()
    print(au.code_verifier)

    au.hash_verifier = au.generate_hash_verifier(au.code_verifier)
    print(au.hash_verifier)
    
    au.base64_verifier = au.generate_base64_verifier(au.hash_verifier.encode())
    print(au.base64_verifier)

if __name__ == '__main__':
    main()