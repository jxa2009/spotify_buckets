# Jason Au
# Functionality of spotify buckets project

#Imports
import random
import hashlib
import base64


#GLOBAL VARIABLES
client_credentials_file = "credentials.txt"
redirect_uri = "localhost:8000"
scope = 'user-library-read playlist-modify-private playlist-read-private user-top-read user-library-modify playlist-modify-public playlist-read-collaborative'  


def read_client_credentials(text_name):
    f = open(text_name)
    client_id = f.readline()
    client_secret = f.readline()
    d['id'] = client_id
    d['secret'] = client_secret
    return d

def generate_code_verifier():
    crypto_random_string = 'abcdefghijklmnopqrstuvwxyz1234567890_.-~'

    lower_bound = 43
    upper_bound = 128
    code_verifier_len = random.randint(lower_bound, upper_bound)

    code_verifier = ''.join(random.choice(crypto_random_string) for _ in range(code_verifier_len))
    return code_verifier

def hash_verifier(code_verifier):
    return hashlib.sha256(code_verifier.encode('utf-8')).hexdigest()
def main():
    #print(read_client_credentials(client_credentials_file))
    code_verifier = generate_code_verifier()
    print(code_verifier)
    print(hash_verifier(code_verifier))

if __name__ == '__main__':
    main()