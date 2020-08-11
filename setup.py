import os
import random
import string

def generateKey():
    return "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))

os.environ["SECRET_KEY"] = generateKey()