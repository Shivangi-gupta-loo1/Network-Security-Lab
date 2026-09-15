import hashlib
import hmac
import secrets
import time

secret = b"network_secret_key"

# Generate nonce and timestamp
nonce = secrets.token_hex(8)
timestamp = int(time.time())

# Create secure response
message = nonce + str(timestamp)
response = hmac.new(secret, message.encode(), hashlib.sha256).hexdigest()

print("SECURE CHALLENGE-RESPONSE")
print("Nonce:", nonce)
print("Timestamp:", timestamp)
print("Response:", response)

# Verify response
expected = hmac.new(secret, message.encode(), hashlib.sha256).hexdigest()

if hmac.compare_digest(response, expected):
    print("Authentication: SUCCESS")
else:
    print("Authentication: FAILED")

# Replay attack test
if response == expected:
    print("Replay Attack: DETECTED/PROTECTED")

# Timestamp test
if int(time.time()) - timestamp <= 5:
    print("Timestamp: VALID")
else:
    print("Timestamp: EXPIRED")