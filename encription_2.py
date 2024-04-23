import hashlib

word = b"This is a test for the encription library haslib 05" # La b es para poder hacer enconde del string, tambien se puede utilizar .encode

encrip_method = hashlib.sha256()

encrip_method.update(word)

print(encrip_method.digest())

print(encrip_method.hexdigest())

print(encrip_method.hexdigest().decode('utf-8'))




