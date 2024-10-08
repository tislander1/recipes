from PySide6.QtWidgets import *
import sys, json, os

from PySide6.QtCore import QAbstractTableModel, Qt
import pandas as pd

file_output = 'test.json'

def remove_blank_rows(table):
    table2 = []
    num_columns = len(table[0])
    blank_row = ['' for ix in range(num_columns)]
    for row in table:
        if row != blank_row:
            table2.append(row)
    return table2

class Tokens():
    def __init__(self):
        self.tokens = {
            'find_button': {'type': 'button', 'label': 'Find', 'button_text': 'Search for:', 'function': 'find_button_function', 'group': 'Controls'},
            'find_textfield': {'type': 'lineedit', 'label': '', 'datatype': 'str', 'default': '', 'group': 'Controls'},
            'find_location': {'type': 'combobox', 'label': 'in field:', 'options': ['Record #', 'Recipe Name', 'Ingredients', 'Instructions', 'Anywhere'], 'datatype': 'str', 'default': 'Name', 'group': 'Controls'},
            'previous_button': {'type': 'button', 'label': 'Previous recipe', 'button_text': 'Previous', 'function': 'previous_button_function', 'group': 'Controls'},
            'next_button': {'type': 'button', 'label': 'Next recipe', 'button_text': 'Next', 'function': 'next_button_function', 'group': 'Controls'},
            'publish_button': {'type': 'button', 'label': 'Publish HTML', 'button_text': 'Publish', 'function': 'publish_button_function', 'group': 'Controls'},
            'publish_table_width': {'type': 'lineedit', 'label': 'Width (mm)', 'datatype': 'str', 'default': '', 'group': 'Controls'},
            'publish_table_height': {'type': 'lineedit', 'label': 'Height (mm)', 'datatype': 'str', 'default': '', 'group': 'Controls'},

            'recipe_number': {'type': 'lineedit', 'label': '#', 'datatype': 'int', 'default': '', 'group': 'Recipe'},
            'recipe_name': {'type': 'lineedit', 'label': 'Name', 'datatype': 'str', 'default': '', 'group': 'Recipe'},
            'ingredients': {'type': 'plaintextedit', 'label': 'Ingredients', 'datatype': 'str', 'default': '', 'group':  'Recipe'},
            'instructions': {'type': 'plaintextedit', 'label': 'Ingredients', 'datatype': 'str', 'default': '', 'group':  'Recipe'},

            'status_window': {'type': 'plaintextedit', 'label': 'Status', 'datatype': 'str', 'default': '', 'group':  'Status'},
        }
        self.config = {}

class TableModel(QAbstractTableModel):
    def __init__(self, data_table, row_count, column_headings, row_headings = []):
        super(TableModel, self).__init__()
        self.data_table = data_table
        num_cols = len(column_headings)
        while len(self.data_table) < row_count:
            self.data_table.append(['' for ix in range(num_cols)])
        self._row_count = row_count
        self._column_headings = column_headings
        self._row_headings = row_headings
    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self.data_table[index.row()][index.column()]
    def rowCount(self, index):
        # The length of the outer list.
        return self._row_count
    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self.data_table[0])
    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._column_headings[section])
            if orientation == Qt.Vertical:
                if self._row_headings and len(self._row_headings) == self._row_count:
                    return str(self._row_headings[section])
                else:
                    return str(section)
    def flags(self, index):
        return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsEditable
    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self.data_table[index.row()][index.column()] = value
            return True

class Window(QDialog):
	# constructor
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Recipe Book")
        token_groups = ['Controls', 'Recipe', 'Status']
        self.setGeometry(100, 100, 700, 500)
        self.layout = QFormLayout()

        self.tok = Tokens()
        
        self.formGroupBoxes = {}
        
        for this_token_group in token_groups:
            self.draw_group_box(this_token_group)

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonBox.accepted.connect(self.write_info_to_file)
        self.buttonBox.rejected.connect(self.reject)
        
        mainLayout = QVBoxLayout()
        for item in self.formGroupBoxes:
            mainLayout.addWidget(self.formGroupBoxes[item][0])
        mainLayout.addWidget(self.buttonBox)
        self.setLayout(mainLayout)

        self.read_info_from_file(file_output)
        self.set_config()

        print('Current configuration at read time: ', self.tok.config)

    def draw_group_box(self, group_name):
        this_group_box = QGroupBox(group_name)
        self.formGroupBoxes[group_name] = [this_group_box,  QFormLayout()]
        for key, value in self.tok.tokens.items():
            if value['group'] == group_name:
                if value['type'] == 'spinbox':
                    setattr(self, key, QSpinBox())
                    obj = getattr(self, key)
                elif value['type'] == 'combobox':
                    setattr(self, key, QComboBox())
                    obj = getattr(self, key)
                    obj.addItems(value['options'])
                elif value['type'] == 'lineedit':
                    setattr(self, key, QLineEdit())
                    obj = getattr(self, key)
                elif value['type'] == 'checkbox':
                    setattr(self, key, QCheckBox())
                    obj = getattr(self, key)
                elif value['type'] == 'plaintextedit':
                    setattr(self, key, QPlainTextEdit())
                    obj = getattr(self, key)
                elif value['type'] == 'table':
                    setattr(self, key, QTableView())
                    obj = getattr(self, key)
                    obj.setModel(TableModel(data_table = value['data'], row_count = value['row_count'], column_headings = value['columns'], row_headings = value['optional_row_labels']))
                elif value['type'] == 'button':
                    setattr(self, key, QPushButton(value['button_text']))
                    obj = getattr(self, key)
                    function_name = value['function']
                    obj.pressed.connect(getattr(self, function_name))
                    x =2
                              
                self.formGroupBoxes[group_name][1].addRow(QLabel(value['label']), obj)  #add row to layout
        self.formGroupBoxes[group_name][0].setLayout(self.formGroupBoxes[group_name][1])

    def set_config(self):
	# run writeInfo method when form is accepted
        for key, val in self.tok.tokens.items():
            if val['type'] in ['lineedit']:
                result = getattr(self, key).text()
            elif val['type'] in ['spinbox']:
                result = getattr(self, key).text()
            elif val['type'] in ['combobox']:
                result = getattr(self, key).currentText()
            elif val['type'] in ['checkbox']:
                result = getattr(self, key).isChecked()
            elif val['type'] in ['plaintextedit']:
                result = getattr(self, key).toPlainText()
            elif val['type'] in ['table']:
                result = getattr(self, key).model().data_table
            elif val['type'] in ['button']:
                pass
            else:
                result = 'ERROR, UNKNOWN TYPE!!'
            if not val['type'] in ['button']:
                self.tok.config[key] = result
        x = 2


    def update_field(self, key, new_value):
	# run writeInfo method when form is accepted
        val = self.tok.tokens[key]
        self.tok.config[key] = new_value
        gui_component = getattr(self, key)
        if val['type'] in ['lineedit']:
            gui_component.setText(new_value)
        elif val['type'] in ['spinbox']:
            gui_component.setValue(int(new_value))
        elif val['type'] in ['combobox']:
            gui_component.setCurrentText(new_value)
        elif val['type'] in ['checkbox']:
            gui_component.setChecked(bool(new_value))
        elif val['type'] in ['plaintextedit']:
            gui_component.setPlainText(new_value)
        elif val['type'] in ['table']:
            gui_component.model().data_table = new_value
        elif val['type'] in ['button']:
            pass
        x = 2
        
    def read_info_from_file(self, filename):
        file_exists = os.path.exists(filename)
        if file_exists:
            with open(filename, 'r') as f:
                self.config = json.load(f)
            for key, val in self.config.items():
                if key in self.__dict__:
                    gui_component = getattr(self, key)
                    if self.tok.tokens[key]['type'] in ['spinbox']:
                        gui_component.setValue(int(val))
                    elif self.tok.tokens[key]['type'] in ['combobox']:
                        gui_component.setCurrentText(val)
                    elif self.tok.tokens[key]['type'] in ['lineedit']:
                        gui_component.setText(val)
                    elif self.tok.tokens[key]['type'] in ['checkbox']:
                        gui_component.setChecked(bool(val))
                    elif self.tok.tokens[key]['type'] in ['plaintextedit']:
                        gui_component.setPlainText(val)
                    elif self.tok.tokens[key]['type'] in ['table']:
                        gui_component.model().data_table = val

	# run writeInfo method when form is accepted
    def write_info_to_file(self):
        self.set_config()
        with open(file_output, 'w') as f:
            json.dump(self.tok.config, f)
            print('Current configuration at write time: ', self.tok.config)
        self.close()

    def find_button_function(self):
        pass
    def previous_button_function(self):
        pass
    def next_button_function(self):
        pass
    def publish_button_function(self):
        pass


# main method
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec())
