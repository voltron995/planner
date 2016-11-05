from passlib.handlers.sha2_crypt import sha256_crypt


def encrypt_password(password: str):
    return sha256_crypt.encrypt(password)


def verify_password(raw_password: str, encrypted_password: str):
    return sha256_crypt.verify(raw_password, encrypted_password)
