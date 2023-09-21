"""
XOR is not recommended as encrypt method for real use cases.
This is just an example of a simple symmetric cypher
"""

def xor_encrypt_decrypt(input_str, key):
    # Convert input string and key to bytes
    input_bytes = input_str.encode('utf-8')
    key_bytes = key.encode('utf-8')
    
    # Make sure key is long enough by repeating it
    key_long = bytearray()
    for i in range(len(input_bytes)):
        key_long.append(key_bytes[i % len(key_bytes)])
    
    # Perform XOR encryption/decryption
    encrypted_bytes = bytearray()
    for i in range(len(input_bytes)):
        encrypted_bytes.append(input_bytes[i] ^ key_long[i])
    
    # Convert the bytes back to a string
    encrypted_str = encrypted_bytes.decode('utf-8', errors='replace')
    
    return encrypted_str

# Test the function
message = "Hello, world!"
key = "key"

# Encrypt the message
encrypted_message = xor_encrypt_decrypt(message, key)
print(f"Encrypted Message: {encrypted_message}")

# Decrypt the message
decrypted_message = xor_encrypt_decrypt(encrypted_message, key)
print(f"Decrypted Message: {decrypted_message}")
