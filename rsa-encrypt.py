def encrypt_with_private_key(message, private_key):
    d, n = private_key
    encrypted_message = []
    for char in message:
        # Convert character to integer using ord()
        char_int = ord(char)
        # Encrypt integer using private key
        encrypted_char = pow(char_int, d, n)
        encrypted_message.append(encrypted_char)
    return encrypted_message

# Assuming private_key is generated from the previous code snippet
private_key = (2753, 3233)  # Replace with the actual private key generated
message = "HELLO"

encrypted_message = encrypt_with_private_key(message, private_key)
print(f"Encrypted message: {encrypted_message}")
