from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class Token():

    def generate_token(self, purpose, key, expiration):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({purpose:key})

    def generate_confirmation_token(self, key, expiration=3600):
        return self.generate_token('confirm', key, expiration)

    def get_key_from_confirmation_token(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
            return data['confirm']
        except:
            return None
