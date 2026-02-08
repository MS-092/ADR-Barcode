import sys
import qtawesome as qta
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame, QSizePolicy, QScrollArea
)
from PySide6.QtCore import Qt, QSize, QRectF, QTimer, QDateTime, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon, QFont, QPalette, QColor, QPainter, QPixmap, QFontMetrics