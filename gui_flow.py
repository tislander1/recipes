import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMainWindow
from PySide6.QtWidgets import QPushButton, QLineEdit, QLabel, QComboBox, QPlainTextEdit


import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Recipe Book")

# class Color(QWidget):

#     def __init__(self, color):
#         super(Color, self).__init__()
#         self.setAutoFillBackground(True)

#         palette = self.palette()
#         palette.setColor(QPalette.Window, QColor(color))
#         self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Recipe Book App")

        layout1 = QVBoxLayout() #main layout for window

        

        layout1.setContentsMargins(0,0,0,0)
        #layout1.setSpacing(20)
        
        #finder tool    -------------------------------------------------------------------
        layout_finder = QHBoxLayout() 
        find_button = QPushButton(" Find")
        find_item = QLineEdit("")
        text1 = QLabel(" in the ")
        find_pulldown = QComboBox()
        find_pulldown.addItems(['Recipe #', 'Recipe Name', 'Ingredients', 'Instructions', 'Anywhere'])
        layout_finder.addWidget(find_button)
        layout_finder.addWidget(find_item)
        layout_finder.addWidget(text1)
        layout_finder.addWidget(find_pulldown)
        layout1.addLayout( layout_finder )

        #Previous/next buttons    -------------------------------------------------------------------
        layout3 = QHBoxLayout() # previous/next tool
        prev_button = QPushButton("Previous Recipe")
        next_button = QPushButton("Next Recipe")
        layout3.addWidget(prev_button)
        layout3.addWidget(next_button)
        layout1.addLayout( layout3 )

        #Publishing -----------------------------------------------------------------------------------
        layout_pub = QHBoxLayout() # publishing tool
        text_pub1 = QLabel(" Enter recipe # or leave blank for all:")
        pub_list = QLineEdit("")
        text_width = QLabel(" Print width (mm):")
        pub_width = QLineEdit("")
        text_height = QLabel(" Height:")
        pub_height = QLineEdit("")
        text_html_file = QLabel(' HTML file:')
        pub_html_file = QLineEdit("recipes.html")
        layout_pub.addWidget(text_pub1)
        layout_pub.addWidget(pub_list)
        layout_pub.addWidget(text_width)
        layout_pub.addWidget(pub_width)
        layout_pub.addWidget(text_height)
        layout_pub.addWidget(pub_height)
        layout_pub.addWidget(text_html_file)
        layout_pub.addWidget(pub_html_file)
        layout1.addLayout( layout_pub )

        #Recipe name and number --------------------------------------------------------------------------
        layout_rec_name = QHBoxLayout()
        text_number = QLabel(' Rec. #:')
        rn_number = QLineEdit("0")
        rn_number.setReadOnly(True)
        rn_number.setMaximumSize(100, 100)
        text_name = QLabel(' Name:')
        rn_name = QLineEdit("")
        layout_rec_name.addWidget(text_number)
        layout_rec_name.addWidget(rn_number)
        layout_rec_name.addWidget(text_name)
        layout_rec_name.addWidget(rn_name)
        layout1.addLayout(layout_rec_name)

        layout_ingr = QHBoxLayout()
        ingredients_text = QLabel(' Ingredients:')
        ingredients_field = QPlainTextEdit('')
        layout_ingr.addWidget(ingredients_text)
        layout_ingr.addWidget(ingredients_field)
        layout1.addLayout(layout_ingr)

        layout_instruct = QHBoxLayout()
        instructions_text = QLabel(' Instructions:')
        instructions_field = QPlainTextEdit('')
        layout_instruct.addWidget(instructions_text)
        layout_instruct.addWidget(instructions_field)
        layout1.addLayout(layout_instruct)


        layout_saver = QHBoxLayout() # publishing tool
        text_dB_file = QLabel(" File:")
        text_dB_name = QLineEdit("recipes.json")
        save_button = QPushButton("Save Recipes")
        spacer = QLabel('      ')
        load_button = QPushButton("Load Recipes")
        layout_saver.addWidget(text_dB_file)
        layout_saver.addWidget(text_dB_name)
        layout_saver.addWidget(save_button)
        layout_saver.addWidget(spacer)
        layout_saver.addWidget(load_button)
        layout_saver.addWidget(spacer)

        layout1.addLayout( layout_saver )

        status_window = QHBoxLayout()
        status_text = QLabel(' Status:')
        status_field = QPlainTextEdit('')
        status_field.setReadOnly(True)
        status_field.setMaximumSize(10000, 100)
        status_window.addWidget(status_text)
        status_window.addWidget(status_field)
        layout1.addLayout(status_window)


        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()