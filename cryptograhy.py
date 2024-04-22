# ENCRIPTACION SIMETRICA

from cryptography.fernet import Fernet

message = "hello word"


key = Fernet.generate_key()

fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print("original message: ", message)
print("encrypted message: ", encMessage)


decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)

# In symmetric-key encryption, the data is encoded and decoded with the same 
# key. This is the easiest way of encryption, but also less secure. 
# The receiver needs the key for decryption, so a safe way need for transferring keys. 
# Anyone with the key can read the data in the middle.