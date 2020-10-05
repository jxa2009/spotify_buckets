# Jason Au
# Functionality of spotify buckets project

#Imports
from authorization import *

from flask import request

#Cannot use spotipy because it is not suitable for web/desktop applications

#GLOBAL VARIABLES
client_credentials_file = "credentials.txt"

#Query Parameters - defined at https://developer.spotify.com/documentation/general/guides/authorization-guide/

#Dictionary containing the endpoints that the app may use
endpoints = {
    "auth" : "https://accounts.spotify.com/authorize"
}

class sign_in:
    def __init__(self):
        query_params = {}
        client_credentials = {}

    def read_client_credentials(self,text_name):
        f = open(text_name)
        client_id = f.readline()
        client_secret = f.readline()
        
        self.client_credentials['id'] = client_id
        self.client_credentials['secret'] = client_secret

    def set_query_params(self,client_id, code_challenge):
        self.query_params = {
            "client_id" : client_id,
            "response_type" :"code",
            "redirect_uri" : "http%3A%2F%2Flocalhost%3A8000%2Flogin",
            # "redirect_uri" : "localhost%3A8000%2Flogin",
            "code_challenge_method" : "S256",
            "code_challenge" :  code_challenge,
            "scope" : 'user-library-read%20playlist-modify-private%20playlist-read-private%20user-top-read%20user-library-modify%20playlist-modify-public%20playlist-read-collaborative' 
        }
        return self.query_params

    def construct_auth_URI(self):
        endpoint = endpoints["auth"] + "?"
        for param in self.query_params.keys():
            endpoint += param + "=" +  self.query_params[param] + '&'
        return endpoint[:-1]


def read_client_credentials(text_name):
    f = open(text_name)
    client_id = f.readline()
    client_secret = f.readline()
    d = {}
    d['id'] = client_id
    d['secret'] = client_secret
    return d

def set_query_params(client_id, code_challenge):
    query_params = {
        "client_id" : client_id,
        "response_type" :"code",
        "redirect_uri" : "http%3A%2F%2Flocalhost%3A8000%2Flogin",
        # "redirect_uri" : "localhost%3A8000%2Flogin",
        "code_challenge_method" : "S256",
        "code_challenge" :  code_challenge,
        "scope" : 'user-library-read%20playlist-modify-private%20playlist-read-private%20user-top-read%20user-library-modify%20playlist-modify-public%20playlist-read-collaborative' 
    }

    return query_params

def construct_auth_URI(query_params):
    endpoint = endpoints["auth"] + "?"
    for param in query_params.keys():
        endpoint += param + "=" +  query_params[param] + '&'
    
    return endpoint[:-1]

def main():
    client_credentials = read_client_credentials(client_credentials_file)
    a = auth()
    a.generate_code_challenge()
    q_param = set_query_params(client_credentials['id'] ,a.getCodeChallenge())
    
    auth_uri = construct_auth_URI(q_param)
    print(auth_uri)


if __name__ == '__main__':
    main()