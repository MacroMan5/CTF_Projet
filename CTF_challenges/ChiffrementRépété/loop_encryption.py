import base64
import random
message_clair = "01253{b@se64_l00ps_4re_fun} 0x55 : Cela vous aidera pour la prochaine épreuve. "

# Fonction pour encoder un message en base64 plusieurs fois
def encode_repeatedly(message, num_repetitions):
    encoded_message = message.encode('utf-8')
    for i in range(num_repetitions):
        encoded_message = base64.b64encode(encoded_message)
    return encoded_message

N = random.randint (28,37)
# Encodez le message en base64 N fois
encoded_message = encode_repeatedly(message_clair, N)

with open ('cipher.txt', 'wb') as f:
    f.write(encoded_message)
    f.close()