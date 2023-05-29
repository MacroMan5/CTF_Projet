#!/usr/bin/env python3
import base64

# Function to try decoding a base64 message, returns None if decoding fails
def try_decode(encoded_message):
    try:
        decoded_message = base64.b64decode(encoded_message).decode('utf-8')
        return decoded_message
    except:
        return None

# Read the contents of the "cipher.txt" file
with open("cipher.txt", 'rb') as f:
    encoded_message = f.read()

# Decode the base64 message repeatedly until the length of the decoded message stops changing
decoded_message = None
while True:
    new_decoded_message = try_decode(encoded_message)
    if new_decoded_message is not None and (decoded_message is None or len(new_decoded_message) != len(decoded_message)):
        decoded_message = new_decoded_message
        encoded_message = decoded_message.encode('utf-8')
    else:
        break

# Print the decoded message
print("Decoded message:", decoded_message)
#write the decoded message to a file
with open('decoded.txt', 'w') as f:
    f.write(decoded_message) # type: ignore
    f.close()
    