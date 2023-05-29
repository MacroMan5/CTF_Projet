
import base64
from datetime import datetime

def generate_password():
    current_time = datetime.now()
    x = current_time.hour
    y = current_time.minute
    z = ["MTA=", "MjA=", "MzA=", "NDA="]
    
    xyz = []
    for value in z:
        zz = int(base64.b64decode(value).decode('utf-8'))
        xyz.append(str(zz + x + y))
    
    password = ''.join(xyz)
    return password

password = generate_password()
print(password)