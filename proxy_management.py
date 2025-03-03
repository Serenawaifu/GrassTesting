from itertools import cycle
import json

with open('config.json', 'r') as f:
    config = json.load(f)

proxies = cycle(config['proxies'])
email_proxy_map = {}

for account in config['accounts']:
    email = account['email']
    email_proxy_map[email] = [next(proxies) for _ in range(config['max_proxies_per_email'])]

def get_proxy_for_email(email):
    if email in email_proxy_map:
        return email_proxy_map[email].pop(0)
    else:
        raise ValueError(f"No proxies available for email: {email}")
