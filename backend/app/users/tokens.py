from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class Token:
    @staticmethod
    def encrypt_token(purpose, key, expiration):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({purpose: key})

    @staticmethod
    def decrypt_token(purpose, token):
        s = Serializer(current_app.config['SECRET_KEY'])
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
