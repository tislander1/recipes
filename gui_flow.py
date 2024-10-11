import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMainWindow, QGroupBox
from PySide6.QtWidgets import QPushButton, QLineEdit, QLabel, QComboBox, QPlainTextEdit

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Recipe Book")

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Recipe Book App")

        self.tok = {}
        self.all_recipes = {
            'codes': {'': 0},
             'data': [{'name': '', 'ingredients': '', 'instructions': ''}]
             }
        self.current_recipe = 0

        print('Loading window.')

        self.layout1 = QVBoxLayout() #main layout for window
        self.layout1.setContentsMargins(0,0,0,0)
        self.layout1.setSpacing(10)
        
        #finder tool    -------------------------------------------------------------------
        layout_finder = QHBoxLayout() 
        find_button = QPushButton(" Find")
        find_button.clicked.connect(self.find_button_handler)
        self.tok['find_item'] = QLineEdit("")
        text1 = QLabel(" in the ")
        self.tok['find_pulldown'] = QComboBox()
        self.tok['find_pulldown'].addItems(['Recipe #', 'Recipe Name', 'Ingredients', 'Instructions', 'Anywhere'])
        layout_finder.addWidget(find_button)
        layout_finder.addWidget(self.tok['find_item'])
        layout_finder.addWidget(text1)
        layout_finder.addWidget(self.tok['find_pulldown'])
        groupbox1 = QGroupBox("Recipe Finder")
        groupbox1.setLayout(layout_finder)
        self.layout1.addWidget(groupbox1)

        #Publishing -----------------------------------------------------------------------------------
        layout_pub = QHBoxLayout() # publishing tool
        text_pub1 = QLabel(" Enter recipe # or leave blank for all:")
        self.tok['publish_list'] = QLineEdit("")
        text_width = QLabel(" Print width (mm):")
        self.tok['publish_width'] = QLineEdit("")
        self.tok['publish_width'].setMaximumWidth(100)
        text_height = QLabel(" Height:")
        pub_height = QLineEdit("")
        pub_height.setMaximumWidth(100)
        text_html_file = QLabel(' HTML file:')
        self.tok['publish_html_file'] =QLineEdit("recipes.html")
        layout_pub.addWidget(text_pub1)
        layout_pub.addWidget(self.tok['publish_list'])
        layout_pub.addWidget(text_width)
        layout_pub.addWidget(self.tok['publish_width'])
        
        layout_pub.addWidget(text_height)
        layout_pub.addWidget(pub_height)
        layout_pub.addWidget(text_html_file)
        layout_pub.addWidget(self.tok['publish_html_file'])
        groupbox_pub = QGroupBox("Publish recipes to HTML")
        groupbox_pub.setLayout(layout_pub)
        self.layout1.addWidget(groupbox_pub)

        #Previous/next buttons    -------------------------------------------------------------------
        layout3 = QHBoxLayout() # previous/next tool
        prev_button = QPushButton("Previous Recipe")
        prev_button.clicked.connect(self.previous_button_handler)
        next_button = QPushButton("Next Recipe")
        next_button.clicked.connect(self.next_button_handler)
        layout3.addWidget(prev_button)
        layout3.addWidget(next_button)
        self.layout1.addLayout( layout3 )

        layout_main_recipe = QVBoxLayout() #main layout for window

        #Main recipe --------------------------------------------------------------------------
        layout_rec_name = QHBoxLayout()
        text_number = QLabel(' Rec. #:')
        self.tok['recipe_number'] = QLineEdit("0")
        self.tok['recipe_number'].setReadOnly(True)
        self.tok['recipe_number'].setMaximumSize(100, 100)
        text_name = QLabel(' Name:')
        self.tok['recipe_name'] = QLineEdit("")
        layout_rec_name.addWidget(text_number)
        layout_rec_name.addWidget(self.tok['recipe_number'])
        layout_rec_name.addWidget(text_name)
        layout_rec_name.addWidget(self.tok['recipe_name'])
        layout_main_recipe.addLayout(layout_rec_name)

        layout_ingr = QHBoxLayout()
        ingredients_text = QLabel(' Ingredients:')
        self.tok['ingredients'] = QPlainTextEdit('')
        layout_ingr.addWidget(ingredients_text)
        layout_ingr.addWidget(self.tok['ingredients'])
        layout_main_recipe.addLayout(layout_ingr)

        layout_instruct = QHBoxLayout()
        instructions_text = QLabel(' Instructions:')
        self.tok['instructions'] = QPlainTextEdit('')
        layout_instruct.addWidget(instructions_text)
        layout_instruct.addWidget(self.tok['instructions'])
        layout_main_recipe.addLayout(layout_instruct)

        groupbox_main_recipe = QGroupBox("Enter a recipe")
        groupbox_main_recipe.setLayout(layout_main_recipe)
        self.layout1.addWidget(groupbox_main_recipe)

        #Save and load the recipe --------------------------------------------------------------------------
        layout_saver = QHBoxLayout() # saver tool
        text_dB_file = QLabel(" File:")
        self.tok['json_file'] = QLineEdit("my recipe book.json")
        save_button = QPushButton("Save Recipes")
        save_button.clicked.connect(self.save_button_handler)
        spacer = QLabel('      ')
        load_button = QPushButton("Load Recipes")
        load_button.clicked.connect(self.load_button_handler)
        layout_saver.addWidget(text_dB_file)
        layout_saver.addWidget(self.tok['json_file'])
        layout_saver.addWidget(save_button)
        layout_saver.addWidget(spacer)
        layout_saver.addWidget(load_button)
        layout_saver.addWidget(spacer)
        self.layout1.addLayout( layout_saver )

        status_panel = QHBoxLayout()
        self.tok['status'] = QPlainTextEdit('')
        self.tok['status'].setReadOnly(True)
        self.tok['status'].setMaximumSize(10000, 100)
        status_panel.addWidget(self.tok['status'])
        status_groupbox = QGroupBox("Program status")
        status_groupbox.setLayout(status_panel)
        self.layout1.addWidget(status_groupbox)

        widget = QWidget()
        widget.setLayout(self.layout1)
        self.setCentralWidget(widget)


    def find_button_handler(self):
        print('Find button clicked.')
    def previous_button_handler(self):
        print('Previous button clicked.')
    def next_button_handler(self):
        print('Next button clicked.')
    def save_button_handler(self):
        print('Save button clicked.')
    def load_button_handler(self):
        print('Load button clicked.')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()