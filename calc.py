from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QGridLayout, QLCDNumber,
                             QToolButton, QApplication, QWidget, QSizePolicy)

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon('calc.png'))
        self.setWindowTitle("Calculator")
        mainMenu = self.menuBar() 
        fileMenu = mainMenu.addMenu('Widok')
        editMenu = mainMenu.addMenu('Edycja')
        viewMenu = mainMenu.addMenu('Pomoc')
    
        calcWidget = CalcWidget()
        self.setCentralWidget(calcWidget)

        self.show()

class CalcWidget(QWidget):
    def __init__(self):
        super().__init__()

        calcLayout = QGridLayout()
        self.setLayout(calcLayout)

        lcdDisplay = QLCDNumber()
        lcdDisplay.display(0)

        clearMemoryButton = Button("MC")
        readMemoryButton = Button("MR")
        setMemoryButton = Button("MS")
        addToMemoryButton = Button("M+")
        subtractFromMemoryButton = Button("M-")

        backspaceButton = Button("\33")
        clearAllButton = Button("C")
        clearButton = Button("CE")
        signButton = Button("\261")
        squareRootButton = Button("\u221a")

        divisionButton = Button("/")
        timesButton = Button("*") 
        minusButton = Button("-")
        plusButton = Button("+")

        percentButton = Button("%")
        reciprocalButton = Button("1/x")
        equalButton = Button("=")

        commaButton = Button(",")
        
        digitButtons = []
        for i in range(10):
            digitButtons.append(Button(str(i)))

        calcLayout.addWidget(lcdDisplay, 0, 0, 1, 6)

        calcLayout.addWidget(clearMemoryButton, 1, 0)
        calcLayout.addWidget(readMemoryButton, 1, 1)
        calcLayout.addWidget(setMemoryButton, 1, 2)
        calcLayout.addWidget(addToMemoryButton, 1, 3)
        calcLayout.addWidget(subtractFromMemoryButton, 1, 4)
        
        calcLayout.addWidget(backspaceButton, 2, 0)
        calcLayout.addWidget(clearAllButton, 2, 2)
        calcLayout.addWidget(clearButton, 2, 1)
        calcLayout.addWidget(signButton, 2, 3)
        calcLayout.addWidget(squareRootButton, 2, 4)

        calcLayout.addWidget(divisionButton, 3, 3)
        calcLayout.addWidget(timesButton, 4, 3)
        calcLayout.addWidget(minusButton, 5, 3)
        calcLayout.addWidget(plusButton, 6, 3)

        calcLayout.addWidget(percentButton, 3, 4)
        calcLayout.addWidget(reciprocalButton, 4, 4)
        calcLayout.addWidget(equalButton, 5, 4, 2, 1)
        
        for i in range(1, 10):
            row = ((9 - i) / 3) + 2
            column = ((i - 1) % 3) + 1
            calcLayout.addWidget(digitButtons[i], row+1, column-1)

        calcLayout.addWidget(digitButtons[0], 6, 0, 1, 2)
        calcLayout.addWidget(commaButton, 6, 2)

def Button(text):
    button = QToolButton()
    button.setText(text)
    size = button.sizeHint()
    size.setHeight(size.height() + 20)
    size.setWidth(max(size.width(), size.height()))
    button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
    return button
    

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
        

        
        
        

        
        
    
