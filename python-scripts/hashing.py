# Hashing: One way function. Same input --> same output.

import hashlib

password = "spaceiscool08!"

data  = password.encode("utf-8")
digest = hashlib.md5(data).hexdigest()

print(f"Password : {password}")
print(f"Hash: {digest}")


#comparing hashed passwords

dif_passwords = ["spiderman$26", "spaceiscool08!", "milacat2091", "blackwidow2@", "a"]

for p in dif_passwords:
    data  = p.encode("utf-8") #converts plainext into raw bytes
    digest = hashlib.sha256(data).hexdigest()  

    print(f"Password : {p}")
    print(f"Hash: {digest}", "\n")