import requests
import base64

def main():
    with open('credentials.txt', 'r') as arq:
        for linha in arq:
            credentials = linha.split()

    CLIENT_ID = credentials[0]
    CLIENT_SECRET = credentials[1]

    CLIENT_CREDENTIALS = f'{CLIENT_ID}:{CLIENT_SECRET}'
    CLIENT_CREDENTIALS_B64 = base64.b64encode(CLIENT_CREDENTIALS.encode())

    token_url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': f'Basic {CLIENT_CREDENTIALS_B64.decode()}'
    }
    data = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, data=data, headers=headers)

    print(f'Status Response: {response.status_code}')
    if response.status_code == 200:
        access_token = response.json()['access_token']
        print("Access token obtained successfully.")
        return access_token
    else:
        print("Error obtaining access token.")
        exit()

if __name__ == '__main__':
    main()