from PySide6.QtCore import QObject, Property, Signal
import threading
import time
from queue import Queue
from task import Task
from core1 import ProcessorCore
from subsystem1 import Subsystem1

class Monitorer(QObject):
    def __init__(self):
        super().__init__()
        self.subsys1 = "help me god"  # Private attribute to store the actual value
        self.ready_queue = ["task1", "task2", "task3"]
        t = threading.Thread(target=self.the_main_func)
        t.start()
        
    def get_subsys1(self):
        return self.subsys1
    
    def set_subsys1(self, value):
        print("the subsys is being called.")
        if self.subsys1 != value:
            self.subsys1 = value
            self.subsys1_changed.emit()  # Emit the signal when the value changes
    
    subsys1_changed = Signal()
    
    subsys1_pyside = Property(str, get_subsys1, set_subsys1, notify=subsys1_changed)

    def get_ready_queue_subsys1_1(self):
        print(f"get is being called!,{self.ready_queue}")
        return self.ready_queue
    
    def set_ready_queue_subsys1_1(self, value):
        self.ready_queue = value
        self.ready_queue_subsys1_1_changed.emit()
        print(f"set is being called! , {value}")

    ready_queue_subsys1_1_changed = Signal()
    
    ready_queue_subsys1_1 = Property(list, get_ready_queue_subsys1_1, set_ready_queue_subsys1_1, notify=ready_queue_subsys1_1_changed)
    

    def monitorer(self, queue_to_check):
        """Monitor changes in a Queue."""
        print(f"[PYSIDE MONITOR] {queue_to_check.queue}")
        previous_state = list(queue_to_check.queue)  # Get the initial state
        while True:
            time.sleep(0.5)
            current_state = list(queue_to_check.queue)  # Current snapshot of the queue
            # print(f"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\current state is: {current_state}")
            if previous_state != current_state:                
                # Extract task IDs or other attributes
                task_ids = [task.task_id for task in current_state]  # Extract task IDs
                # Pass the extracted list to another function
                self.set_ready_queue_subsys1_1(task_ids)
                # Update the previous state
                previous_state = current_state
                

    def the_main_func(self):
        # Initialize arrays for subsystems and tasks
        subsystem_tasks = [[] for _ in range(4)]  # Create a list to store tasks for each subsystem
        subsys_resource = []

        # Step 1: Read resource allocation for each subsystem
        # print("Enter resources for each subsystem:")
        # for i in range(4):
        #     line = input()
        #     subsys_resource.append(list(map(int, line.split())))

        # print("Subsystem Resources:", subsys_resource)

        # # Step 2: Read tasks for each subsystem
        # print("\nEnter tasks for each subsystem (end input for a subsystem with #):")
        # for i in range(4):
        #     print(f"\nSubsystem {i + 1}:")
        #     tasks = []
        #     while True:
        #         line = input()
        #         if line == "$":  # Separator for subsystems
        #             break

        #         task_details = line.split()
        #         task_name = task_details[0]
        #         task_len = int(task_details[1])
        #         resource1 = int(task_details[2])
        #         resource2 = int(task_details[3])
        #         enter_time = int(task_details[4])

        #         # Add specific fields based on the subsystem
        #         if i == 0:  # Subsystem 1
        #             dest_cpu = int(task_details[5])
        #             task = {
        #                 "name": task_name,
        #                 "len": task_len,
        #                 "resource1": resource1,
        #                 "resource2": resource2,
        #                 "enter_time": enter_time,
        #                 "dest_cpu": dest_cpu,
        #             }
        #         elif i == 1:  # Subsystem 2
        #             task = {
        #                 "name": task_name,
        #                 "len": task_len,
        #                 "resource1": resource1,
        #                 "resource2": resource2,
        #                 "enter_time": enter_time,
        #             }
        #         elif i == 2:  # Subsystem 3
        #             period = int(task_details[5])
        #             num_repeats = int(task_details[6])
        #             task = {
        #                 "name": task_name,
        #                 "len": task_len,
        #                 "resource1": resource1,
        #                 "resource2": resource2,
        #                 "enter_time": enter_time,
        #                 "period": period,
        #                 "num_repeats": num_repeats,
        #             }
        #         elif i == 3:  # Subsystem 4
        #             pre_requisite = task_details[5]
        #             task = {
        #                 "name": task_name,
        #                 "len": task_len,
        #                 "resource1": resource1,
        #                 "resource2": resource2,
        #                 "enter_time": enter_time,
        #                 "pre_requisite": pre_requisite,
        #             }

        #         tasks.append(task)

        #     subsystem_tasks[i] = tasks

        # # Step 3: Print the collected tasks
        # for i, tasks in enumerate(subsystem_tasks):
        #     print(f"\nTasks for Subsystem {i + 1}:")
        #     for task in tasks:
        #         print(task)
        self.set_ready_queue_subsys1_1(["task1", "task2", "task3"])
        
        subsystem1 = Subsystem1(r1_count=5, r2_count=3, time_slice=2)
        
        task1 = Task(task_id=1, execution_time=10, weight=2, required_r1=1, required_r2=1)
        task2 = Task(task_id=2, execution_time=8, weight=3, required_r1=1, required_r2=2)
        task3 = Task(task_id=3, execution_time=12, weight=1, required_r1=1, required_r2=2)
        task4 = Task(task_id=4, execution_time=10, weight=2, required_r1=1, required_r2=1)
        task5 = Task(task_id=5, execution_time=8, weight=3, required_r1=1, required_r2=2)
        task6 = Task(task_id=6, execution_time=12, weight=1, required_r1=1, required_r2=2)
        task7 = Task(task_id=7, execution_time=10, weight=2, required_r1=1, required_r2=1)
        task8 = Task(task_id=8, execution_time=8, weight=3, required_r1=1, required_r2=2)
        task9 = Task(task_id=9, execution_time=12, weight=1, required_r1=1, required_r2=2)

        subsystem1.add_task(task1)
        subsystem1.add_task(task2)
        subsystem1.add_task(task3)
        subsystem1.add_task(task4)
        subsystem1.add_task(task5)
        subsystem1.add_task(task6)
        subsystem1.add_task(task7)
        subsystem1.add_task(task8)
        subsystem1.add_task(task9)

        subsystem1.start()
        
        threading.Thread(target=self.monitorer, args=(subsystem1.ready_queues[0],)).start()
        

        # threading.Barrier
        
        time.sleep(20)

        subsystem1.stop()

        myqueue = ["1"]
        for i in range(5):
            time.sleep(1)
            myqueue.append("task"+ str(i+1))
            self.set_ready_queue_subsys1_1(myqueue)
    

    def additional_task(self, hi):
        print(f"Additional thread running with argument: {hi}")
        # Perform any additional work in this thread
        for i in range(5):
            time.sleep(1)
            print(f"Additional task iteration {i}: {hi}")
        
