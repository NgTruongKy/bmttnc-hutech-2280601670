from flask import Flask, request , jsonify
from Cipher.Caeser import CaeserCipher
app = Flask(__name__)

# CAESER CIPHER ALGORITHM
  
caeser_ciper = CaeserCipher()

@app.route("/api/caeser/encrypt", methods = ["POST"])
def caeser_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caeser_ciper.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caeser/decrypt", methods = ["POST"])
def caeser_decypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caeser_ciper.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

#main funtion 

if __name__ == "__main__" :
    app.run(host = "0.0.0.0", port = 5000 , debug = True)