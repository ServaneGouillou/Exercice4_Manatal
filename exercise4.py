#ex 4 : 3h

###### Part 1 : Authentification #########
### We authentificate with the Twitter API

client_key = 'CLIENT_KEY'
client_secret = 'CLIENT_SECRET'

import base64

key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

import requests

base_url = 'https://api.twitter.com/'
auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

# auth_resp.status_code #Check if the authentification succeeded

access_token = auth_resp.json()['access_token']


###### Part 2 : Getting the information #########

twitter_url = input("Enter the Twitter url: ")

def get_number_of_followers(twitter_url):
    """
    The function will give the number of followers of any twitter account given its url.

    Parameters
    -----------
    twitter_url : string : url of the twitter account
    -----------

    """

    list_url = twitter_url.split("/")
    username = list_url[-1]

    headers = {
    'Authorization': 'Bearer {}'.format(access_token)    
    }

    url = '{}2/users/by/username/' + username + '?user.fields=public_metrics'
    url = url.format(base_url)

    resp = requests.get(url, headers=headers)

    #resp.status_code #Check if the request succeeded

    data = resp.json()

    if 'errors' in data :
        return 'There is an error. Check if the Twitter User does exist'

    else :
        number_of_followers = str(data['data']['public_metrics']['followers_count'])
        name = data ['data']['name']

        return (name + ' has got ' + number_of_followers + ' followers on Twitter.')

print(get_number_of_followers(twitter_url))
