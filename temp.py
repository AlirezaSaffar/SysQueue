import threading
import time
from queue import Queue
from task import Task
from core1 import ProcessorCore
from subsystem1 import Subsystem1
from subsystem2 import Subsystem2
from subsystem3 import Subsystem3
from subsystem4 import Subsystem4
from realtimetask import Task as tt
from ss4task import Task as t
subsystem1 = Subsystem1(r1_count=5, r2_count=8, time_slice=2)
subsystem2 = Subsystem2(r1_count=5, r2_count=3)
subsystem3 = Subsystem3(r1_count=5, r2_count=3,subsystem1=subsystem1,subsystem2=subsystem2)
task1 = Task(task_id=1, execution_time=10, weight=2, required_r1=1, required_r2=1)
task2 = Task(task_id=2, execution_time=8, weight=3, required_r1=1, required_r2=1)
task3 = Task(task_id=3, execution_time=12, weight=1, required_r1=1, required_r2=2)
task7 = Task(task_id=7, execution_time=8, weight=1, required_r1=1, required_r2=2)
task8 = Task(task_id=8, execution_time=5, weight=1, required_r1=1, required_r2=2)
subsystem2.add_task(task7)
subsystem2.add_task(task8)

task4 = tt(task_id=4, execution_time=2, weight=1, required_r1=4, required_r2=1, period=5)
task5 = tt(task_id=5, execution_time=2, weight=1, required_r1=1, required_r2=4, period=3)
task6 = tt(task_id=6, execution_time=2, weight=1, required_r1=1, required_r2=4, period=5)
subsystem1.add_task(task1)
subsystem1.add_task(task2)
subsystem1.add_task(task3)

subsystem1.start()
# subsystem = Subsystem4(5,5)
subsystem2.start()

# task1 = t(1, 5, 2, 2, []) 
# task2 = t(2, 3, 5, 1, [1]) 
# task3 = t(3, 4, 1, 5, [1]) 
# task4 = t(4, 2, 2, 3, [2, 3]) 

# subsystem.add_task(task1)
# subsystem.add_task(task2)
# subsystem.add_task(task3)
# subsystem.add_task(task4)




subsystem3.add_task(task4)
subsystem3.add_task(task5)
subsystem3.add_task(task6)
subsystem3.start()


# subsystem3.start()

   
waiting_queue_thread = threading.Thread(target=subsystem1.manage_waiting_queue)
waiting_queue_thread.daemon = True
waiting_queue_thread.start()
