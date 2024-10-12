def encrypt(plaintext, a, b):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha(): 
            encrypted_char = (a * (ord(char) - ord('a')) + b) % 26 + ord('a')
            encrypted_text += chr(encrypted_char)
        else:
            encrypted_text += char 
    return encrypted_text.upper()

def decrypt(ciphertext, a_inv, b):
    ciphertext = ciphertext.lower()
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  
            decrypted_char = (a_inv * ((ord(char) - ord('a')) - b)) % 26 + ord('a')
            decrypted_text += chr(decrypted_char)
        else:
            decrypted_text += char  
    return decrypted_text

a = 17
b = 20
a_inv = 23  

txt_to_encrypt = "attackatonce"

encrypted_txt = encrypt(txt_to_encrypt, a, b)
decrypted_txt = decrypt(encrypted_txt, a_inv, b)

print(f"a={a}, a_inv={a_inv}\n")

print("Encryption")
print("Plaintext: ", txt_to_encrypt)
print("Cyphertext:", encrypted_txt)

print("\nDecryption")
print("Plaintext: ", decrypted_txt)
print("Cyphertext: ", encrypted_txt)
