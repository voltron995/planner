from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class Token:

    @staticmethod
    def get_secret_key():
        return current_app.config['SECRET_KEY']

    @classmethod
    def encrypt_token(cls, purpose, key, expiration):
        s = Serializer(cls.get_secret_key(), expiration)
        return s.dumps({purpose: key})

    @classmethod
    def decrypt_token(cls, purpose, token):
        s = Serializer(cls.get_secret_key())
        try:
            data = s.loads(token)
            return data[purpose]
        except:
            return None

    @classmethod
    def encrypt_confirmation_token(cls, key, expiration=3600):
        return cls.encrypt_token('confirm', key, expiration)

    @classmethod
    def decrypt_confirmation_token(cls, token):
        return cls.decrypt_token('confirm', token)
