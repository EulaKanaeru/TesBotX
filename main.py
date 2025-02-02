import requests
import json
import random
import string
import time

# Daftar nama umum untuk email agar terlihat lebih natural
NAMES = ["john", "michael", "sarah", "jessica", "robert", "david", "linda", "james", "emily", "william", "daniel"]
DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "protonmail.com", "aol.com", "icloud.com"]

# Fungsi buat email acak yang lebih natural
def generate_random_email():
    name = random.choice(NAMES)  
    number = random.randint(10, 9999)  
    domain = random.choice(DOMAINS)  
    return f"{name}{number}@{domain}"

# Fungsi buat wallet address acak dengan format yang lebih alami
def generate_random_wallet():
    return "0x" + ''.join(random.choices("abcdef" + string.digits, k=40))  

# Fungsi buat nama acak yang lebih realistis
def generate_random_name():
    first_name = random.choice(NAMES).capitalize()
    last_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10))).capitalize()
    return first_name, last_name

url = "https://api.getwaitlist.com/api/v1/waiter"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    'Accept': "application/json",
    'Accept-Encoding': "gzip, deflate",
    'Content-Type': "application/json",
    'Referer': "https://ecosapiens.xyz/",
    'Origin': "https://ecosapiens.xyz",
    'Sec-Fetch-Site': "same-origin",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Dest': "empty",
    'Accept-Language': "en-US,en;q=0.9,id;q=0.8"
}

# Loop otomatis berjalan selamanya
while True:
    email = generate_random_email()
    wallet_address = generate_random_wallet()
    first_name, last_name = generate_random_name()

    payload = json.dumps({
        "waitlist_id": 24495,
        "referral_link": "https://ecosapiens.xyz/pages/airdrop?ref_id=S4FP3TR4Q",
        "heartbeat_uuid": "",  
        "widget_type": "WIDGET_1",
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "answers": [
            {
                "question_value": "What is your EVM wallet address?",
                "answer_value": wallet_address
            }
        ]
    })

    try:
        response = requests.post(url, data=payload, headers=headers)
        response.encoding = response.apparent_encoding

        if response.status_code == 200:
            print(f"✅ {email} | {wallet_address} | OK | is_spam: {is_spam}")
        else:
            print(f"❌ {email} | {wallet_address} | is_spam: {is_spam} | ERROR {response.status_code}")

    except Exception as e:
        print(f"⚠️ ERROR: {e}")

    # Delay random antara 30 - 90 detik agar terlihat natural
    time.sleep(random.randint(30, 90))
