# Jason Au
# Functionality of spotify buckets project

#Imports
from authorization import *



#Cannot use spotipy because it is not suitable for web/desktop applications

#GLOBAL VARIABLES
client_credentials_file = "credentials.txt"

#Query Parameters - defined at https://developer.spotify.com/documentation/general/guides/authorization-guide/

#Dictionary containing the endpoints that the app may use
endpoints = {
    "auth" : "https://accounts.spotify.com/authorize",
    "token" : "https://accounts.spotify.com/api/token"
}

class sign_in:

    # Initialize the sign_in object with some variables it will need
    def __init__(self):
        self.query_params = {}
        self.client_credentials = {}
        self.auth_uri = ""

    def setCodeChallenge(self,code_challenge):
        self.query_params["code_challenge"] = code_challenge
    # Take the name of a text file in the same directory as this file
    # Return a dictionary with the client ID and Secret, shouldn't need the secret for the purpose of this app
    def read_client_credentials(self):
        f = open(client_credentials_file)
        client_id = f.readline()
        client_secret = f.readline()
        
        self.client_credentials['id'] = client_id.rstrip()
        self.client_credentials['secret'] = client_secret.rstrip()

    # Set the query params object with some data that is static
    def set_query_params(self):
        self.query_params = {
            "client_id" : self.client_credentials['id'],
            "response_type" :"code",
            "redirect_uri" : "http%3A%2F%2Flocalhost%3A8000%2Fbuckets",
            # "redirect_uri" : "localhost%3A8000%2Flogin",
            "code_challenge_method" : "S256",
            "scope" : 'user-library-read%20playlist-modify-private%20playlist-read-private%20user-top-read%20user-library-modify%20playlist-modify-public%20playlist-read-collaborative' 
        }
        return self.query_params

    # Use the query params to generate an auth uri
    def construct_auth_URI(self):
        endpoint = endpoints["auth"] + "?"
        for param in self.query_params.keys():
            endpoint += param + "=" +  self.query_params[param] + '&'
        self.auth_uri = endpoint

    def process_sign_in(self):
        self.read_client_credentials()
        self.set_query_params()
        self.construct_auth_URI()

    def getClientID(self):
        return self.client_credentials['id']

    def getRedirectURI(self):
        return self.query_params["redirect_uri"]
def main():
    # client_credentials = read_client_credentials(client_credentials_file)

    a = auth()
    a.generate_code_challenge()

    # q_param = set_query_params(client_credentials['id'] ,a.getCodeChallenge())
    
    # auth_uri = construct_auth_URI(q_param)
                                                                                                                                                                          
    si = sign_in(a.getCodeChallenge())
    si.read_client_credentials(client_credentials_file)
    si.set_query_params()
    si.construct_auth_URI()
    print(si.auth_uri)


if __name__ == '__main__':
    main()