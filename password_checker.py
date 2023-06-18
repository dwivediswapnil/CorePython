import requests
import hashlib


#Hashing a password
#Never store a password in string format.

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/'+query_char
    res = requests.get(url)
    #response 400 isn't good
    print(res)
    if res.status_code !=200:
        raise RuntimeError(f'Error fetching : {res.status_code},check api and try again')
    return res

def get_pwd_leaks_count(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text)
    print(hashes)

def pwned_api_check(password):
    #Check pwd if it exists in API Response
    #'utf-8' becoz unicode objects must be encoded b4 hashing.
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print(sha1pwd)
 
    # first 5 characters and the remaining
    first5_char,tail = sha1pwd[:5],sha1pwd[5:]
    response = request_api_data(first5_char)
    print(first5_char,tail)
    return get_pwd_leaks_count(response,tail)

pwned_api_check('123')

