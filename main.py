# import necessary module and classes:
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget)
from custom_widget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
    
    def initialize_ui(self):
        """
        Initalize the main window and display its content
        """
        self.setWindowTitle("Layout Vertical")
        self.setGeometry(50, 50, 600,800)
        self.display_contents()
    def display_contents(self):
        """
        Create Layout and add its widgets
        """
        # Create the vertical layout
        verical_layout = QVBoxLayout()
        # Add widgets
        verical_layout.addWidget(Color("crimson"))
        verical_layout.addWidget(Color("pirple"))
        verical_layout.addWidget(Color("green"))
        # Create the container for the layout
        container = QWidget()
        container.setLayout(verical_layout)
        # Display the container to the main window
        self.setCentralWidget(container)
# Run the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())