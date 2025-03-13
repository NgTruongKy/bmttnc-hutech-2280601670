class VigenerCipher:
    def __init__(self, key):
        pass

    def Vigenere_Cipher(self, plainText,key):
        encrypted_text = ""
        key_index = 0
        for char in plainText : 
            if char.isalpha():
                key_Shift = ord(key[key_index]) - ord('A')
                if char.islower():
                    shift = ord('a')
                else:
                    shift = ord('A')
                encrypted_text += chr((ord(char) - shift + key_Shift) % 26 + shift)
                key_index = (key_index + 1) % len(key)
            else:
                encrypted_text += char
        return encrypted_text
    def Vigenere_decrypt(self, encrypted_text,key):
        decrypted_text = ""
        key_index = 0
        for char in encrypted_text : 
            if char.isalpha():
                key_Shift = ord(key[key_index]) - ord('A')
                if char.islower():
                    shift = ord('a')
                else:
                    shift = ord('A')
                decrypted_text += chr((ord(char) - shift - key_Shift) % 26 + shift)
                key_index = (key_index + 1) % len(key)
            else:
                decrypted_text += char
        return decrypted_text
            

    