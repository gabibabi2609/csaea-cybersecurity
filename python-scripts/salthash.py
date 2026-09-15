import hashlib
import os

plaintext_password = "blackwidow20"
password = plaintext_password.encode("utf-8")

# 1. regular hash, no salt, for two users, same password --> indentical hashes
hash_a = hashlib.sha256(password).hexdigest()
hash_b = hashlib.sha256(password).hexdigest()

print("No salt:")
print(f" User A: {hash_a}")
print(f" User B: {hash_b}")

#Add salt. each user will get their own random SALT
salt_a = os.urandom(16)
salt_b = os.urandom(16)

print(f" User A: {salt_a}")
print(f" User B: {salt_b}")

salt_hash_a = hashlib.sha256(salt_a + password).hexdigest()
salt_hash_b = hashlib.sha256(salt_b + password).hexdigest()

print("\nWith salt:")
print(f" User A with salt + hash: {salt_hash_a}")
print(f" User B hash: {salt_hash_b}")