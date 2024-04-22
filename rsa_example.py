import rsa

publicKey, privateKey = rsa.newkeys(512)

message = "hello word"

encMessage = rsa.encrypt(message.encode(),
                         publicKey)

print("original message: ", message)
print("encripted message: ", encMessage)


decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("decripted message: ", decMessage)

# In Asymmetric-key Encryption, we use two keys a 
# public key and a private key. The public key is 
# used to encrypt the data and the private key is used to 
# decrypt the data. By the name, the public key can be public 
# (can be sent to anyone who needs to send data). No one has your private key, so no one in the middle can read your data.