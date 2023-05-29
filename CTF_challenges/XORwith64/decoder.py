import base64
import base64
import binascii

# Fonction pour décoder un message avec XOR
def xor_decode(encoded_message, key):
    return "".join(chr(ord(c) ^ key) for c in encoded_message)

# Fonction pour décoder un message de base64 et hexadecimal plusieurs fois
def decode_repeatedly(encoded_message, num_repetitions):
    decoded_message = encoded_message
    for i in range(num_repetitions):
        try:
            # Décodage en hexadecimal
            decoded_message = binascii.unhexlify(decoded_message)
            # Décodage en base64
            decoded_message = base64.b64decode(decoded_message)
        except:
            return None
    return decoded_message.decode('utf-8')

# Votre clé pour le XOR
key = 0x55

# Lire le message encodé depuis le fichier
with open('cipher.txt', 'rb') as f:
    encoded_message = f.read()

# Initialisez N à 1
N = 1
while True:
    # Essayez de décoder le message N fois
    decoded_message = decode_repeatedly(encoded_message, N)

    # Si le décodage a réussi
    if decoded_message is not None:
        # Essayez de décoder le message avec XOR
        try:
            decoded_message = xor_decode(decoded_message, key)
            # Si le message décodé commence par le préfixe de drapeau attendu, imprimer le message
            if decoded_message.startswith("01253{"):
                print(decoded_message)
                with open('flag.txt', 'w') as f:
                    f.write(decoded_message)
                    f.close()
                break
        except:
            pass
    # Incrémentez N pour la prochaine boucle
    N += 1
if N > 50:
    print("Condition arreter la boucle apres 50 iterations")