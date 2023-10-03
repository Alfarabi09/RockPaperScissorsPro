import hmac
import os
import hashlib

class CryptoUtil:
    @staticmethod
    def generate_key():
        return os.urandom(32)  # 256-bit key

    @staticmethod
    def compute_hmac(message, key):
        return hmac.new(key, message.encode(), hashlib.sha256).hexdigest()