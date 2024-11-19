import hashlib

def create_hash(text : str):
    h = hashlib.sha1(bytes(text, 'utf-8'))
    h.digest()
    return h.hexdigest()