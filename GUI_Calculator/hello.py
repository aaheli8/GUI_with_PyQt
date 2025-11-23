import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QPushButton

app = QApplication([])

window = QWidget()
# window.setWindowTitle("PyQt App")
# window.setGeometry(100,100,280,80)
# helloMsg = QLabel("<h1>Hello, World!</h1>", parent = window)
# helloMsg.move(60, 15)

window.setWindowTitle("QGridLayout")

layout = QGridLayout()
layout.addWidget(QPushButton("Button (0,0)"), 0, 0)
layout.addWidget(QPushButton("Button (0,1)"),0,1)
layout.addWidget(QPushButton("Button (0,2)"),0,2)
layout.addWidget(QPushButton("Button (1,0)"),1,0)
layout.addWidget(QPushButton("Button (1,1)"),1,1)
layout.addWidget(QPushButton("Button (1,2)"),1,2)
layout.addWidget(QPushButton("Button (2,0)"),2,0)
layout.addWidget(QPushButton("Button (2,1) + 2 Columns Span"), 2, 1, 1, 2)

window.setLayout(layout)
window.show()
sys.exit(app.exec())