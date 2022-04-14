from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor, QPalette

class Color(QWidget):
    def __init__(self,color="hot pink"):
        super().__init__()
        # turn on the autoFill 
        self.setAutoFillBackground(True)
        # Create palette which is wrap (غلاف)
        palette = self.palette()
        # Set the color of the wrap (غلاف) to color parameter 
        palette.setColor(QPalette.Window,QColor(color))
        # set the this class to wear the wrap (غلاف) 
        self.setPalette(palette)
        