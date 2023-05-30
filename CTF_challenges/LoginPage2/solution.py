
import base64
from datetime import datetime

def generate_password():
    current_time = datetime.now()
    x = current_time.hour
    y = current_time.minute
    z = ["MTA=", "MjA=", "MzA=", "NDA="]
    
    xyz = []
    n = 1
    for value in z:  
        zz = int(base64.b64decode(value).decode('utf-8'))
        sum_value = zz + x + y
        print(f"Valeur {n} ajouté au mot de passe complet, x, and y: {sum_value}")
        xyz.append(str(zz + x + y))
        n += 1
    password = ''.join(xyz)
    print(f"Mot de passe complet: {password}")
    return password

password = generate_password()
print(password)
