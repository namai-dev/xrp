import requests
import time

def send_withdrawal_request():
    url = "https://xrpspin.com/api.php?act=withdrawXrp"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://xrpspin.com",
        "Referer": "https://xrpspin.com/withdraw.php",
        "Connection": "close"
    }
    payload = {
        "confirm": 0,
        "payout_value": 0.000025,
        "password": "f]N8n\"$c&X%ADQs",
        "xrpAddr": "rNxp4h8apvRis6mJf9Sh8C6iRxfrDWN7AV",
        "distTag": "356823014"
    }
    response = requests.post(url, headers=headers, json=payload)
    print("Response:", response.status_code)

# Run the task every 5 minutes
while True:
    send_withdrawal_request()
    time.sleep(300)  # 5 minutes (300 seconds)

