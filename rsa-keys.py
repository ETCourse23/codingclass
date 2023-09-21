import random

# Function to calculate the Greatest Common Divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate the modular multiplicative inverse
def modinv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Generate two distinct prime numbers p and q (for demonstration, these are small primes)
p, q = 61, 53

# Calculate n = p * q
n = p * q

# Calculate the totient function phi(n) = (p - 1) * (q - 1)
phi_n = (p - 1) * (q - 1)

# Generate public key exponent e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
e = random.randrange(2, phi_n)
while gcd(e, phi_n) != 1:
    e = random.randrange(2, phi_n)

# Generate private key exponent d such that (d * e) % phi(n) = 1
d = modinv(e, phi_n)

# Public key: (e, n), Private key: (d, n)
public_key = (e, n)
private_key = (d, n)

print(f"Public key: {public_key}")
print(f"Private key: {private_key}")
