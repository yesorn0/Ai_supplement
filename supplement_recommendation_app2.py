# supplement_recommendation_app2.py

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from ui_modal import Ui_Form
import webbrowser

class ModalLikeWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("추천 결과")

        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlag(Qt.Window)

        self.current_url = "https://example.com"
        self.update_url_button()

        self.pushButton_url.clicked.connect(self.open_url)

    def set_url(self, url):
        self.current_url = url
        self.update_url_button()

    def update_url_button(self):
        self.pushButton_url.setText(self.current_url)

    def open_url(self):
        webbrowser.open(self.current_url)
