import sys
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from pyside_back import Monitorer
import os

if __name__ == "__main__":
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    qml_file = os.path.join(script_dir, "main.qml")  
    qmlRegisterType(Monitorer, "Pyside_handler", 1, 0, "Monitor")
    
    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.load("main.qml")

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec())