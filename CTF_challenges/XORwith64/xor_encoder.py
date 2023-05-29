import base64
import binascii
import os
import random
from config import key

# Flag et message chiffré
flag = "01253{X0R_Base64_Hexadecimal_l00ps}"

# Fonction pour encoder un message avec XOR
def xor_encode(message, key):
    return "".join(chr(ord(c) ^ key) for c in message)

# Fonction pour encoder en base64 et hexadecimal plusieurs fois
def encode_repeatedly(message, num_repetitions):
    encoded_message = message.encode('utf-8')
    for i in range(num_repetitions):
        # Encodage en base64
        encoded_message = base64.b64encode(encoded_message)
        # Encodage en hexadecimal
        encoded_message = binascii.hexlify(encoded_message)
    return encoded_message

# Votre clé pour le XOR
key = key

# Encode le message chiffré avec XOR
xor_encoded_message = xor_encode(flag, key)

N = random.randint(10,20)
# Encode le message en base64 et hexadecimal N fois
encoded_message = encode_repeatedly(xor_encoded_message, N)

with open('cipherV2.txt', 'wb') as f:
    f.write(encoded_message)
    f.close() 
