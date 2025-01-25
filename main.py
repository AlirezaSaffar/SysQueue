import sys
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from pyside_back import Monitorer
import os
import threading
import time
from queue import Queue
from task import Task
from core1 import ProcessorCore
from subsystem1 import Subsystem1

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

    # subsystem1 = Subsystem1(r1_count=5, r2_count=3, time_slice=2)

    # task1 = Task(task_id=1, execution_time=10, weight=2, required_r1=1, required_r2=1)
    # task2 = Task(task_id=2, execution_time=8, weight=3, required_r1=1, required_r2=2)
    # task3 = Task(task_id=3, execution_time=12, weight=1, required_r1=1, required_r2=2)

    # subsystem1.add_task(task1)
    # subsystem1.add_task(task2)
    # subsystem1.add_task(task3)

    # subsystem1.start()

   
    # waiting_queue_thread = threading.Thread(target=subsystem1.manage_waiting_queue)
    # waiting_queue_thread.daemon = True
    # waiting_queue_thread.start()

   
    # time.sleep(20)

    # subsystem1.stop()
    