from cryptography.fernet import Fernet

message = "hello word"


key = Fernet.generate_key()

fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print("original message: ", message)
print("encrypted message: ", encMessage)
