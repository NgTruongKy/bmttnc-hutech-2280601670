import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QMessageBox 
from ui.caeser import Ui_Dialog
import requests

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btnen.clicked.connect(self.call_api_encrypt)
        self.ui.btnde.clicked.connect(self.call_api_decrypt)
        self.ui.


        self.show()

    def call_api_encrypt(self):
     
        url = "http://127.0.0.1:5000/api/caeser/encrypt"
        payload = {
            "plain_text": self.ui.txtplain.toPlainText(),
            "key": self.ui.txtkey.toPlainText()
        }
        try :
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtcipher.setPlainText(data['encrypted_message'])


                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encryption Successful")
                msg.exec_()
            else:
                print("Error")
        except requests.exceptions.RequestException as e:
            print("Error while calling API")
            print("Enror: %s"  %e.message)
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caeser/decrypt"
        payload = {
            "cipher_text": self.ui.txtcipher.toPlainText(),
            "key": self.ui.txtkey.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txtplain.setPlainText(data['decrypted_message'])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decryption Successful")
                msg.exec_()
            else:
                print("Error")
        except requests.exceptions.RequestException as e:
            print("Error while calling API")
            print("Error: %s" % e.message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
