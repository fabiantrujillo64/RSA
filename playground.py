import time
e = 5
n = 299
d = 53

LUT_encryption = dict()
LUT_decryption = dict()

def encrypt_message(msg):
    encrypted_msg = ""
    for i in msg:
        if i in LUT_encryption:
          encrypted_msg += LUT_encryption[i]
        else:  
            numerize = ord(i)
            encrypt = pow(numerize, e, n)
            LUT_encryption[i] = unichr(encrypt)
            encrypted_msg += unichr(encrypt)
    return encrypted_msg         
        
def decrypt_message(msg):
    decrypted_msg = ""
    for i in msg:
        if i in LUT_decryption:
            decrypted_msg += LUT_decryption[i]
        else:
            numerize = ord(i)
            decrypt = pow(numerize, d, n)
            LUT_decryption[i] = unichr(decrypt)
            decrypted_msg += unichr(decrypt)
    return decrypted_msg


message = "mississippi"

start = time.time()
final_encrypted_message = encrypt_message(message)
print final_encrypted_message
print decrypt_message(final_encrypted_message)
end = time.time()
print(end - start)