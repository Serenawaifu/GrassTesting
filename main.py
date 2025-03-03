import json
import asyncio
from account_registration import register_account
from proxy_management import get_proxy_for_email
from telegram_bot import send_message, start_bot

with open('config.json', 'r') as f:
    config = json.load(f)

async def main():
    for account in config['accounts']:
        email = account['email']
        password = account['password']
        referral_code = account['referral_code']
        try:
            proxy = get_proxy_for_email(email)
            register_account(email, password, referral_code)
            send_message(config['telegram_chat_id'], f'Registered account: {email} with proxy: {proxy}')
        except ValueError as e:
            send_message(config['telegram_chat_id'], str(e))
        
        await asyncio.sleep(1)  # To avoid rate limiting

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_in_executor(None, start_bot)
    loop.run_forever()
