import hashlib
import base64
import random

class auth:
    def __init__(self):
        self.code_verifier = ''
        self.hash_verifier = ''
        self.base64_verifier = ''
        self.code_challenge = ''

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
    # Returns encoded string as a string without byte object type
    def generate_base64_verifier(self, hash_verifier_string):
        enc = base64.standard_b64encode(hash_verifier_string)
        enc = enc.decode()
        
        return enc

    # Uses the classes functions to generate the code challenge all in one call
    # Returns the generated code challenge
    def generate_code_challenge(self):
        self.code_verifier = self.generate_code_verifier()
        self.hash_verifier = self.generate_hash_verifier(self.code_verifier)
        self.base64_verifier = self.generate_base64_verifier(self.hash_verifier.encode())
        self.code_challenge = self.base64_verifier
    
    def getCodeChallenge(self):
        return self.code_challenge

    def getCodeVerifier(self):
        return self.code_verifier


def main():
    #print(read_client_credentials(client_credentials_file))
    au = auth()

    au.code_verifier = au.generate_code_verifier()
    print("Code verifier: ", au.code_verifier)

    au.hash_verifier = au.generate_hash_verifier(au.code_verifier)
    print("Hash verifier: ", au.hash_verifier)
    
    au.base64_verifier = au.generate_base64_verifier(au.hash_verifier.encode())
    print("Base64 Verifier: ", au.base64_verifier)


if __name__ == '__main__':
    main()