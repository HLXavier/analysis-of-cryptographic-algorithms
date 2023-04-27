from AES import AES
import tripleDes

def aesEncrypt(plain_text, key, rounds=10):
    aes = AES(key)
    aes.nr = rounds
    return aes.encrypt(plain_text)

def aesDecrypt(cipher_text, key, rounds=10):
    aes = AES(key)
    aes.nr = rounds
    return aes.decrypt(cipher_text)

def desEncrypt(plain_text, key, rounds):
    tdes = tripleDes.triple_des(key, tripleDes.CBC, rounds=rounds)
    return tdes.encrypt(plain_text)

def desDecrypt(plain_text, key, rounds):
    tdes = tripleDes.triple_des(key, tripleDes.CBC, rounds=rounds)
    return tdes.decrypt(plain_text)

names = ['lenna', 'panda', 'fruit']
