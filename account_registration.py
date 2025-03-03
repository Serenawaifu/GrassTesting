import requests
from fake_useragent import UserAgent
from loguru import logger

def register_account(email, password, referral_code):
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random,
        'Content-Type': 'application/json'
    }
    data = {
        'email': email,
        'password': password,
        'referral_code': referral_code
    }
    
    response = requests.post('https://example.com/api/register', headers=headers, json=data)
    
    if response.status_code == 201:
        logger.info(f'Successfully registered account: {email}')
    else:
        logger.error(f'Failed to register account: {email} - {response.text}')
