import sys
import requests
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from ui.rsa_cipher import Ui_rsa_cipher


class RSACipherApp(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_rsa_cipher()
        self.ui.setupUi(self)

        # Kết nối các nút với hàm xử lý
        self.ui.btn_gen_keys.clicked.connect(self.generate_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def generate_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Keys generated successfully!")
            else:
                QMessageBox.critical(self, "Error", "Failed to generate keys.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request error: {str(e)}")

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txt_plain_text.toPlainText(),
            "key_type": "public"  # Sử dụng khóa công khai để mã hóa
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data['encrypted_message'])
                QMessageBox.information(self, "Success", "Encryption successful!")
            else:
                QMessageBox.critical(self, "Error", "Encryption failed.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request error: {str(e)}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key_type": "private"  # Sử dụng khóa riêng tư để giải mã
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data['decrypted_message'])
                QMessageBox.information(self, "Success", "Decryption successful!")
            else:
                QMessageBox.critical(self, "Error", "Decryption failed.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request error: {str(e)}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txt_info.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_sign.setPlainText(data['signature'])
                QMessageBox.information(self, "Success", "Message signed successfully!")
            else:
                QMessageBox.critical(self, "Error", "Signing failed.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request error: {str(e)}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_info.toPlainText(),
            "signature": self.ui.txt_sign.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if data["verified"]:
                    QMessageBox.information(self, "Success", "Signature verification successful!")
                else:
                    QMessageBox.warning(self, "Warning", "Signature verification failed!")
            else:
                QMessageBox.critical(self, "Error", "Verification failed.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Request error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RSACipherApp()
    window.show()
    sys.exit(app.exec_())
