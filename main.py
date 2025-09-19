import csv
import requests
import time

API_KEY = "47e43303-394e-4889-9b08-de2767d74002"   # <-- yaha apna API key daalna
ASSISTANT_ID = "c6b59ccb-5b5e-4847-af58-98c1d5191068"

def make_call(phone_number, name=None):
    url = "https://api.vapi.ai/call"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "assistantId": ASSISTANT_ID,
        "type": "outboundPhoneCall",
        "customer": {
            "number": phone_number,
            "name": name if name else "Customer"
        },
        "phoneNumberId": "d40c48bf-6b99-4b53-93b2-50e12a8b75af"
    }
    response = requests.post(url, json=payload, headers=headers)
    try:
        data = response.json()
    except:
        data = response.text
    print(f"📞 Calling {phone_number} -> {data}")

# CSV se numbers read karna
with open("demo.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        phone = row['Phone Number']
        name = row.get('Name', None)

        # ✅ Clean and format number
        phone = phone.strip().replace(" ", "")
        if not phone.startswith("+"):
            phone = "+91" + phone

        print(f"📞 Final dialing number: {phone}")  # Debugging

        make_call(phone, name)
        time.sleep(2)  # 2 sec gap between calls