import hashlib

def password_hash(password):
    ret = ""
    password = str(password)
    ret = hashlib.sha256(password.endcode()).hexdigest()
    return ret

def check_password(password, hash):
    password_hashed = hashlib.sha256(password.encode()).hexdigest()
    if password_hashed == hash:
        return True
    else:
        return False