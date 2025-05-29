import sys
import pickle
import webbrowser
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QStringListModel
from PyQt5 import uic
from scipy.io import mmread
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import linear_kernel

# 리소스 로딩 (.qrc → .py로 변환된 아이콘 리소스 등)
import resources_rc

# 모달창 로직 불러오기
from supplement_recommendation_app2 import ModalLikeWindow

# .ui 파일 로드
form_window = uic.loadUiType('./supplement_recommendation_app.ui')[0]

class SupplementApp(QMainWindow, form_window):
    def __init__(self):
        super().__init__()
        self.ui = form_window()
        self.ui.setupUi(self)

        # 아이콘 설정
        self.setWindowIcon(QIcon(":/perilla_favicon2.png"))

        # 검색 버튼 연결 (버튼 objectName이 'pushButton_search'라고 가정)
        self.ui.pushButton.clicked.connect(self.show_modal)

    def show_modal(self):
        self.result_window = ModalLikeWindow(self)
        self.result_window.set_url("https://your-supplement.com")  # 필요시 동적 설정 가능
        self.result_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SupplementApp()
    window.show()
    sys.exit(app.exec_())
