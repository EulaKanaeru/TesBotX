import requests
import json
import random
import string
import time
from flask import Flask
from threading import Thread

# Data nama dan domain lebih natural
FIRST_NAMES = ["John", "Michael", "Sarah", "Jessica", "Robert", "David", "Linda", "James", "Emily", "William"]
LAST_NAMES = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin"]
DOMAINS = ["gmail.com", "yahoo.com", "outlook.com", "protonmail.com", "icloud.com"]

# Fungsi buat email yang lebih natural
def generate_random_email():
    first = random.choice(FIRST_NAMES).lower()
    last = random.choice(LAST_NAMES).lower()
    number = random.randint(10, 999)
    domain = random.choice(DOMAINS)
    return f"{first}.{last}{number}@{domain}"

# Fungsi buat wallet address acak
def generate_random_wallet():
    return "0x" + ''.join(random.choices("abcdef" + string.digits, k=40))

# Fungsi buat nama lengkap lebih natural
def generate_random_name():
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    return first_name, last_name

# URL API
url = "https://api.getwaitlist.com/api/v1/waiter"

# Header request
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/126.0.0.0",
    'Accept': "application/json",
    'Accept-Encoding': "gzip, deflate, br",
    'Content-Type': "application/json",
    'Referer': "https://ecosapiens.xyz/",
    'Origin': "https://ecosapiens.xyz",
    'Sec-Fetch-Site': "same-origin",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Dest': "empty",
    'Accept-Language': "en-US,en;q=0.9,id;q=0.8"
}

# Fungsi utama
def run_script():
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
                json_response = response.json()
                is_spam = json_response.get("is_spam", False)
                status_text = "✅ SUCCESS" if not is_spam else "⚠️ SPAM"
                print(f"{status_text}: {email} | {wallet_address} | is_spam: {is_spam}")
            else:
                print(f"❌ ERROR {response.status_code}: {email} | {wallet_address}")

        except Exception as e:
            print(f"⚠️ ERROR: {e}")

        # Delay untuk menghindari deteksi spam
        delay_time = random.randint(60, 180)
        print(f"⏳ Waiting {delay_time} seconds...\n")
        time.sleep(delay_time)

# Inisialisasi Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# Jalankan Flask di thread terpisah
def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Mulai proses Flask dan script utama
if __name__ == "__main__":
    thread1 = Thread(target=run_script)
    thread1.start()
    
    thread2 = Thread(target=run_flask)
    thread2.start()
        
