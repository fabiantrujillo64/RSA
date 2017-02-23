e = 5
n = 299
d = 53

def encrypt_message(msg):
    encrypted_msg = ""
    for i in msg:
        numerize = ord(i)
        encrypt = pow(numerize, e, n)
        encrypted_msg += unichr(encrypt)
    return encrypted_msg         
        
def decrypt_message(msg):
    for i in msg:
        numerize = ord(i)
        decrypt = pow(numerize, d, n)
        print decrypt


message = "mississippi"

final_encrypted_message = encrypt_message(message)
decrypt_message(final_encrypted_message)