##https://stackoverflow.com/questions/6048576/how-to-generate-a-fixed-length-hash-based-on-current-date-and-time-in-python
import time
import hashlib

hash = hashlib.sha1()

def create_hash():
    hash = hashlib.sha1()
    hash.update(str(time.time()).encode('utf-8'))
    UUID = hash.hexdigest()
    return UUID