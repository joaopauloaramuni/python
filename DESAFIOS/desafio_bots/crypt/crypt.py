from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64decode
from base64 import b64encode
import os

# Chave de encriptação
rsa_pass = os.getenv("rsa_pass")


def save_pemfile(private_key, public_key):
    """
    Save PEM key into the file
    :param private_key
    :param public_key
    :return:
    """
    with open('private.pem', 'wb') as file:
        file.write(private_key)

    with open('public.pem', 'wb') as file:
        file.write(public_key)

    print("Pem file save.")


class Crypt(object):
    """
    Crypt class
    """

    @staticmethod
    def encrypt(string):
        """
        Encrypt string msg
        :param string
        :return: encrypt string
        """
        if string is None:
            return string
        key = RSA.importKey(open('public.pem').read())
        cipher = PKCS1_v1_5.new(key)
        return b64encode(cipher.encrypt(string))

    @staticmethod
    def decrypt(string):
        """
        Decrypt string msg
        :param string
        :return: decrypt string
        """
        key = RSA.importKey(open('private.pem').read())
        cipher = PKCS1_v1_5.new(key)
        return cipher.decrypt(b64decode(string), '** decryption error **')

    @staticmethod
    def generate_rsa(bits=2048):
        """
        Generate an RSA keypair with an exponent of 65537 in PEM format
        :param bits The key length in bits
        :return: private key and public key
        """
        new_key = RSA.generate(bits, e=65537)

        private_key = new_key.exportKey(passphrase=rsa_pass)
        public_key = new_key.publickey().exportKey()

        # save_pemfile(private_key, public_key)

        return private_key, public_key
