from PyQt5.QtWidgets import (QLineEdit , QLabel ,QPushButton , QProgressBar , QWidget , QApplication,
                             QVBoxLayout , QMainWindow , QDateEdit , QComboBox , QCheckBox)
import sys
from PyQt5.QtCore import Qt , QPropertyAnimation, QRect
import pandas as pd
import csv
import matplotlib.pyplot as plt
from PyQt5.QtGui import QPalette, QColor

#need to add button animation and icons
#second page with a journal entry
#need to add try except incase user doesnt fill in all the questions

class inventorymanager(QMainWindow):
    def __init__(self):
        super().__init__()

        #we need to type the name of the potion or item , then add the rarity 
        # using a qcombobox(weapons , armor , potions , scrolls )
        #set the value of the item
        self.setWindowTitle("Dungeon Loot Tracker")
        self.input_item = QLineEdit(self)

        self.choose_item_type = QComboBox(self)
        self.choose_item_type.addItems(['weapon' , 'armour' , 'potion' , 'scroll'])

        self.item_value = QLineEdit(self)

        self.is_it_enchanted = QCheckBox(self)
        
        self.save_data = QPushButton('seal the scroll' , self)
        self.initUI()
    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(QLabel('Dungeon Loot Tracker'))
        vbox.addWidget(self.input_item)
        vbox.addWidget(self.choose_item_type)
        vbox.addWidget(QLabel('item value(in gold coins):'))
        vbox.addWidget(self.item_value)
        vbox.addWidget(QLabel('is it enchanted?'))
        vbox.addWidget(self.is_it_enchanted)
        vbox.addWidget(self.save_data)
        container = QWidget()
        container.setLayout(vbox)

        self.setCentralWidget(container)

        self.save_data.clicked.connect(self.save_inventory)
        self.save_data.clicked.connect(self.pulse_button)
        self.input_item.setObjectName('input_item')
        self.choose_item_type.setObjectName('choose_item')
        self.item_value.setObjectName('item_val')
        self.is_it_enchanted.setObjectName('enchanted')
        self.save_data.setObjectName('save')
        self.setStyleSheet(f'''
                           
                        QMainWindow{{
                           
                             background-image: url("scroll2.jpg");
                             background-repeat: no-repeat;
                             background-position: center;
                             background-color: rgba(255, 255, 255, 0.2);

                        }}  

                        QLineEdit{{
                            
                            padding: 10px;
                            border: 3px solid black;
                            border-radius:8px;
                            font-size: 30px;
                            selection-color: black;
                            selection-background-color: yellow;
                            font-family: 'Arial Black';
                            color: black;
                            background-color: rgba(255, 255, 255, 0.5);
                            
                           }}
            
                            QLabel{{
                             font-size:35px;
                             font-weight : bold;
                             font-family: 'Papyrus';
                             
                             color : #000000;
                                                }}
                           
                            QPushButton{{
                                
  
                                border: 2px solid #A67C52;
                                border-radius: 10px;
                                padding: 8px;
                                font-family: 'Arial Black';
                                font-size: 40px;
                                  
                                background-position: bottom;
                                background-color: rgba(255, 255, 255, 0.5);
                                
                                color : #000000;   
                                

                            }}
                           QComboBox{{
                            
                            border : 6px solid;
                            border-radius : 10px;
                            padding: 8px;
                            font-family: 'Papyrus';
                            font-size: 40px;

                            background-color :rgba(255, 255, 255, 0.5);
                            color: #000000;  /* readable ink */
                            selection-background-color: #FFD700;  
                            selection-color: #3B2F2F; 

                           }}
                            


                        



         ''')
    def save_inventory(self):
        input = self.input_item.text()
        category = self.choose_item_type.currentText()
        value = self.item_value.text()
        is_it_enchanted = self.is_it_enchanted.isChecked()
        

        with open ('inventory.csv' , 'a') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['item name' , 'type' , 'value' , 'is it enchanted'])
            writer.writerow([input , category , value , is_it_enchanted])

    def pulse_button(self):
        original_geometry = self.save_data.geometry()

        self.anim = QPropertyAnimation(self.save_data, b"geometry")
        self.anim.setDuration(300)
        self.anim.setStartValue(original_geometry)
        self.anim.setEndValue(QRect(
            original_geometry.x() - 5,
            original_geometry.y() - 5,
            original_geometry.width() + 10,
            original_geometry.height() + 10
        ))
        self.anim.setLoopCount(2)
        self.anim.setDirection(QPropertyAnimation.Forward)
        self.anim.start()



app = QApplication([])
app.setStyle('Fusion')
inv_app = inventorymanager()
inv_app.show()
palette = QPalette()
palette.setColor(QPalette.Window, QColor('#D4AF37'))
palette.setColor(QPalette.WindowText, Qt.white)
app.setPalette(palette)


sys.exit(app.exec())