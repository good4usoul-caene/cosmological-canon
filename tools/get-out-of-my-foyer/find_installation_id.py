import time
import jwt
import requests
import json

# Your App ID (we just stored this)
APP_ID = "2265924"

# Read the private key from the file we validated
with open(r"C:\Users\good4\Downloads\gardener-cosmological-canon.2025-11-10.private-key.pem", "rb") as f:
    private_key = f.read()

# Create JWT for the GitHub App
now = int(time.time())
payload = {
    "iat": now - 60,  # issued 1 minute ago
    "exp": now + (10 * 60),  # expires in 10 minutes
    "iss": APP_ID
}

jwt_token = jwt.encode(payload, private_key, algorithm="RS256")
print(f"JWT created successfully")

# Get installations for this app
headers = {
    "Authorization": f"Bearer {jwt_token}",
    "Accept": "application/vnd.github+json"
}

try:
    resp = requests.get("https://api.github.com/app/installations", headers=headers)
    print(f"Status code: {resp.status_code}")
    
    if resp.status_code == 200:
        installations = resp.json()
        print(f"\nFound {len(installations)} installation(s):")
        
        for installation in installations:
            print(f"  Installation ID: {installation['id']}")
            print(f"  Account: {installation['account']['login']}")
            print(f"  Account type: {installation['account']['type']}")
            print(f"  Created: {installation['created_at']}")
            print()
    else:
        print(f"Error response: {resp.text}")

except Exception as e:
    print(f"Error: {e}")
    print("Make sure you have 'pip install pyjwt requests' installed")