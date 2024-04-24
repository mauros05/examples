from hashlib import blake2b

FILES_HASH_PERSON = b'MyApp Files Hash'
BLOCK_HASH_PERSON = b'MyApp Block Hash'

h = blake2b(digest_size=32, person=FILES_HASH_PERSON)
h.update(b'the same content')
print(h.hexdigest())


h = blake2b(digest_size=32, person=BLOCK_HASH_PERSON)
h.update(b'the same content')
print(h.hexdigest())