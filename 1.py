import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("特效按钮示例")
        self.setGeometry(100, 100, 400, 200)

        # 创建一个按钮
        self.button = QPushButton("特效按钮", self)
        self.button.setGeometry(150, 80, 100, 40)

        # 设置按钮样式
        self.button.setStyleSheet(
            """
            QPushButton {
                background-color: #3498db;  /* 正常状态下的背景颜色 */
                border: 1px solid #2980b9;  /* 边框样式 */
                color: white;  /* 字体颜色 */
                border-radius: 5px;  /* 圆角 */
                font-size: 16px;  /* 字体大小 */
            }
            QPushButton:hover {
                background-color: #2980b9;  /* 鼠标悬停时的背景颜色 */
            }
            QPushButton:pressed {
                background-color: #2070a0;  /* 按下时的背景颜色 */
            }
            """
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
