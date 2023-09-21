import hashlib

# Your text message
message = "Hello, World!"

# Create a SHA-256 hash object
sha256 = hashlib.sha256()

# Update the hash object with the message bytes
sha256.update(message.encode('utf-8'))

# Get the hexadecimal representation of the hash
hashed_message = sha256.hexdigest()

# Print the hashed message
print("SHA-256 Hash:", hashed_message)
