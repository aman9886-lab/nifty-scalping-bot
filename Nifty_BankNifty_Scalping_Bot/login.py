
from kiteconnect import KiteConnect

api_key = "your_api_key_here"
api_secret = "your_api_secret_here"

kite = KiteConnect(api_key=api_key)
print("Login URL:", kite.login_url())

# After visiting login_url and authorizing, get request_token and paste below
request_token = input("Enter Request Token: ")

data = kite.generate_session(request_token, api_secret=api_secret)
print("Access Token:", data["access_token"])
