import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
import deepl

# deepl
auth_key =  "3c2a2b46-c014-0af9-0b29-934eb3d52b33:fx" # Replace with your key
translator = deepl.Translator(auth_key)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("IWS")

        # 设置窗口大小
        self.setFixedSize(800, 600)

        # 加载自定义背景图片
        bg_image = QPixmap("胡桃.jpg")  # 替换为您自己的背景图片文件路径
        self.background = QLabel(self)
        self.background.setPixmap(bg_image)
        self.background.setAlignment(Qt.AlignCenter)  # 让背景图片居中

        # 创建文本输入框
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Input")
        self.text_input.setFixedSize(800, 50)  # 设置文本显示框的大小
        # 设置文本输入框样式，包括字体、字号和字体颜色
        self.text_input.setStyleSheet(
            """
            QLineEdit {
                background-color: transparent;  /* 背景色设置为透明 */
                font-family: Arial, Helvetica, sans-serif;  /* 设置字体 */
                font-size: 20px;  /* 设置字号 */
                font-weight: bold;  /* 设置字体为加粗 */
                color: #36d7b7;  /* 设置字体颜色 */
            }
            """
        )


        # 创建文本显示框
        self.text_display = QTextEdit(self)
        self.text_display.setReadOnly(True)
        self.text_display.setFixedSize(800, 80)  # 设置文本显示框的大小
        self.text_display.setStyleSheet(
            """
            QTextEdit {
                border: none;  /* 隐藏边框 */
                background-color: transparent;  /* 背景色设置为透明 */
                font-family: Arial, Helvetica, sans-serif;  /* 设置字体 */
                font-size: 20px;  /* 设置字号 */
                font-weight: bold;  /* 设置字体为加粗 */
                color: #67f2d1;  /* 设置字体颜色 */
                
            }
            """
        )

        # 创建按钮
        self.button = QPushButton("Trans", self)
        self.button.clicked.connect(self.display_text)
        self.button.setFixedSize(100, 40)  # 设置按钮的宽度和高度
        # 设置按钮样式
        self.button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;  /* 背景色设置为透明 */
                border: 1px solid #3498db;  /* 边框样式 */
                color: #3498db;  /* 字体颜色 */
                border-radius: 5px;  /* 圆角 */
                font-size: 16px;  /* 字体大小 */
            }
            QPushButton:hover {
                background-color: #76CBB2;  /* 鼠标悬停时的背景色 */
                color: white;  /* 字体颜色变为白色 */
            }
            QPushButton:pressed {
                background-color: #C1C5E3;  /* 按下时的背景色 */
            }
            """
        )

        # 创建布局管理器
        layout = QGridLayout()
        layout.addWidget(self.text_input, 2, 0, 1, 1)
        layout.addWidget(self.text_display, 1, 0, 1, 2)
        layout.addWidget(self.button, 3, 1, 1, 1)
        layout.addWidget(self.background, 0, 0, 4, 3)
        self.setLayout(layout)

    def display_text(self):
        text = self.text_input.text()
        result = translator.translate_text(text, target_lang="EN-US")
        self.text_display.append(str(result))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
