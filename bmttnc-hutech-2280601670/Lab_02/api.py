from flask import Flask, request , jsonify
from Cipher.Caeser import CaeserCipher

from Lab_02.Cipher.Caeser import CaeserCipher
from Lab_02.Vigenere.Vigenere_cipher import VigenerCipher

from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the ciphers
caeser_cipher = CaeserCipher()
vigenere_cipher = VigenerCipher()

@app.route("/api/caeser/encrypt", methods=["POST"])
def caeser_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caeser_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caeser/decrypt", methods=["POST"])
def caeser_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caeser_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.Vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.Vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
Vigener_Cipher=VigenerCipher()
@app.route("/api/vigenere/encrypt", methods = ["POST"])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = Vigener_Cipher.Vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/vigenere/decrypt", methods = ["POST"])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = Vigener_Cipher.Vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})
#main funtion 

if __name__ == "__main__" :
    app.run(host = "0.0.0.0", port = 5000 , debug = True)