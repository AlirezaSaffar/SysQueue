from PySide6.QtCore import QObject, Property, Signal
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
from ss4task import Task as t_4
from logger import LoggerThread

class Monitorer(QObject):
    def __init__(self):
        super().__init__()
        self.subsys1 = "help me god"
        self.ready_queue_subsys1_1 = []
        self.ready_queue_subsys1_2 = []
        self.ready_queue_subsys1_3 = []
        self.ready_queue_subsys2 = []
        self.ready_queue_subsys3 = []
        self.ready_queue_subsys4 = []
        
        t = threading.Thread(target=self.the_main_func)
        t.start()

    #########################################################################
    # setter and getter for subsys1 queue 1:#################################
    def get_ready_queue_subsys1_1(self):
        # print(f"get is being called!,{self.ready_queue_subsys1_1}")
        return self.ready_queue_subsys1_1
    
    def set_ready_queue_subsys1_1(self, value):
        self.ready_queue_subsys1_1 = value
        self.ready_queue_subsys1_1_changed.emit()
        # print(f"set is being called! , {value}")
    #########################################################################
        
    #########################################################################
    # setter and getter for subsys1 queue 2:#################################
    def get_ready_queue_subsys1_2(self):
        # print(f"get is being called!,{self.ready_queue_subsys1_2}")
        return self.ready_queue_subsys1_2
    
    def set_ready_queue_subsys1_2(self, value):
        self.ready_queue_subsys1_2 = value
        self.ready_queue_subsys1_2_changed.emit()
        # print(f"set is being called! , {value}")
    #########################################################################
    
    #########################################################################
    # setter and getter for subsys1 queue 3:#################################
    def get_ready_queue_subsys1_3(self):
        # print(f"get is being called!,{self.ready_queue_subsys1_3}")
        return self.ready_queue_subsys1_3
    
    def set_ready_queue_subsys1_3(self, value):
        self.ready_queue_subsys1_3 = value
        self.ready_queue_subsys1_3_changed.emit()
        # print(f"set is being called! , {value}")
    #########################################################################
    
    #########################################################################
    # setter and getter for subsys2:#########################################
    def get_ready_queue_subsys2(self):
        # print(f"get is being called!,{self.ready_queue_subsys2}")
        return self.ready_queue_subsys2
    
    def set_ready_queue_subsys2(self, value):
        # print()
        # print(f"set is being called. for subsys2 with the value of {value}////////////////////////////////////////////////////")
        self.ready_queue_subsys2 = value
        self.ready_queue_subsys2_changed.emit()
        # print(f"set is being called! , {value}")
    #########################################################################
    
    #########################################################################
    # setter and getter for subsys3:#########################################
    def get_ready_queue_subsys3(self):
        # print(f"get is being called!,{self.ready_queue_subsys3}")
        return self.ready_queue_subsys3
    
    def set_ready_queue_subsys3(self, value):
        # print()
        # print(f"set is being called. for subsys3 with the value of {value}///////////////////////////////////////////////////")
        self.ready_queue_subsys3 = value
        self.ready_queue_subsys3_changed.emit()
        # print(f"set is being called! , {value}")
    #########################################################################

    #########################################################################
    # setter and getter for subsys4:#########################################
    def get_ready_queue_subsys4(self):
        # print(f"get is being called!,{self.ready_queue_subsys4}")
        return self.ready_queue_subsys4
    
    def set_ready_queue_subsys4(self, value):
        self.ready_queue_subsys4 = value
        self.ready_queue_subsys4_changed.emit()
        # print(f"44444444444444444444444444444444444444444444444   set is being called! , {value} 4444444444444444444444444444444")
    #########################################################################
    
    ready_queue_subsys1_1_changed = Signal()
    ready_queue_subsys1_2_changed = Signal()
    ready_queue_subsys1_3_changed = Signal()
    ready_queue_subsys2_changed = Signal()
    ready_queue_subsys3_changed = Signal()
    ready_queue_subsys4_changed = Signal()
    
    back_end_ready_queue_subsys1_1 = Property(list, get_ready_queue_subsys1_1, set_ready_queue_subsys1_1, notify=ready_queue_subsys1_1_changed)
    back_end_ready_queue_subsys1_2 = Property(list, get_ready_queue_subsys1_2, set_ready_queue_subsys1_2, notify=ready_queue_subsys1_2_changed)
    back_end_ready_queue_subsys1_3 = Property(list, get_ready_queue_subsys1_3, set_ready_queue_subsys1_3, notify=ready_queue_subsys1_3_changed)
    back_end_ready_queue_subsys2 = Property(list, get_ready_queue_subsys2, set_ready_queue_subsys2, notify=ready_queue_subsys2_changed)
    back_end_ready_queue_subsys3 = Property(list, get_ready_queue_subsys3, set_ready_queue_subsys3, notify=ready_queue_subsys3_changed)
    back_end_ready_queue_subsys4 = Property(list, get_ready_queue_subsys4, set_ready_queue_subsys4, notify=ready_queue_subsys4_changed)
    
    ###########################################################################################################################################
                
                
    def monitorer_name(self, queue_to_check, setter_name):
        # print(f"[PYSIDE MONITOR] {queue_to_check.queue}")
        previous_state = list(queue_to_check.queue)  # Get the initial state
        while True:
            time.sleep(0.01)
            current_state = list(queue_to_check.queue)  # Current snapshot of the queue
            # print(f"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\current state is: {current_state}")
            if previous_state != current_state:                
                task_ids = [task.task_id for task in current_state]
                # print(f"[PYSIDE FUNC MONITOR] here is the updated list{task_ids} , this is the one calling: {setter_name}")
                # Pass the extracted list to another function
                if setter_name == "set_ready_queue_subsys1_1":
                    self.set_ready_queue_subsys1_1(task_ids)
                elif setter_name == "set_ready_queue_subsys1_2":
                    self.set_ready_queue_subsys1_2(task_ids)
                elif setter_name == "set_ready_queue_subsys1_3":
                    self.set_ready_queue_subsys1_3(task_ids)
                elif setter_name == "set_ready_queue_subsys4":
                    
                    self.set_ready_queue_subsys4(task_ids)

                previous_state = current_state
                
    # def monitorer_tuple(self, queue_to_check, setter_name):
    # # Extract the initial state of the PriorityQueue
    #     # print(f"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\[MONITOR TUPLE] is called for the {queue_to_check} for {setter_name}")
    #     previous_state = list(queue_to_check.queue)  # Internal access for PriorityQueue
    #     while True:
    #         time.sleep(0.1)
    #         # Get the current snapshot of the PriorityQueue
    #         current_state = list(queue_to_check.queue)  # Access elements in priority order

    #         if previous_state != current_state:
    #             # Extract task IDs from the current state
    #             task_ids = [task[1].task_id for task in current_state]  # task[1] holds the actual task object
    #             # Call the appropriate setter function
    #             if setter_name == "set_ready_queue_subsys2":
    #                 self.set_ready_queue_subsys2(task_ids)
    #             elif setter_name == "set_ready_queue_subsys3":
    #                 self.set_ready_queue_subsys3(task_ids)

    #             # Update the previous state
    #             previous_state = current_state
    
    def monitorer_tuple(self, queue_to_check, setter_name):
        previous_state = list(queue_to_check.queue)  # Internal snapshot of the queue

        while True:
            time.sleep(0.01)  
            current_state = list(queue_to_check.queue)  # Current snapshot of the queue

            if previous_state != current_state:
                # Extract task IDs from each entry
                task_ids = []
                for item in current_state:
                    # If it's a 2-tuple: (priority, task)
                    if len(item) == 2:
                        # item[1] is the task object
                        task_ids.append(item[1].task_id)
                    # If it's a 3-tuple: (priority, something, task)
                    elif len(item) == 3:
                        # item[2] is the task object
                        task_ids.append(item[2].task_id)
                    else:
                        # Handle other formats or log an error
                        print(f"Unexpected tuple format in queue: {item}")

                # Call the appropriate setter function
                if setter_name == "set_ready_queue_subsys2":
                    self.set_ready_queue_subsys2(task_ids)
                elif setter_name == "set_ready_queue_subsys3":
                    self.set_ready_queue_subsys3(task_ids)
                previous_state = current_state
        
        ###############################################################
        # this is for input:###########################################
        # subsys_resource, subsystem_tasks = self.collect_input()

        #this is for debugge
        # print("Subsystem Resources:", subsys_resource)
        # for i, tasks in enumerate(subsystem_tasks):
        #     print(f"\nTasks for Subsystem {i + 1}:")
        #     for task in tasks:
        #         print(task)
        ###############################################################
        
        ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    def the_main_func(self):
        subsystem1 = Subsystem1(r1_count=5, r2_count=3, time_slice=2)
        subsystem2 = Subsystem2(r1_count=5, r2_count=3)
        subsystem3 = Subsystem3(r1_count=5, r2_count=3, subsystem1 = subsystem1, subsystem2 = subsystem2)
        subsystem4 = Subsystem4(r1_count=5, r2_count=9)
        
        task1 = Task(task_id=1, execution_time=10, weight=2, required_r1=1, required_r2=1)
        task2 = Task(task_id=2, execution_time=8, weight=3, required_r1=1, required_r2=2)
        task3 = Task(task_id=3, execution_time=12, weight=1, required_r1=1, required_r2=2)
        task4 = Task(task_id=4, execution_time=10, weight=2, required_r1=1, required_r2=1)
        task5 = Task(task_id=5, execution_time=8, weight=3, required_r1=1, required_r2=2)
        task6 = Task(task_id=6, execution_time=12, weight=1, required_r1=1, required_r2=2)
        task7 = Task(task_id=7, execution_time=10, weight=2, required_r1=1, required_r2=1)
        task8 = Task(task_id=8, execution_time=8, weight=3, required_r1=1, required_r2=2)
        task9 = Task(task_id=9, execution_time=12, weight=1, required_r1=1, required_r2=2)
        
        task10 = tt(task_id=10, execution_time=2, weight=1, required_r1=4, required_r2=1, period=5)
        task11 = tt(task_id=11, execution_time=2, weight=1, required_r1=1, required_r2=4, period=3)
        task12 = tt(task_id=12, execution_time=2, weight=1, required_r1=1, required_r2=4, period=5)
        task13 = tt(task_id=13, execution_time=2, weight=1, required_r1=4, required_r2=1, period=5)
        task14 = tt(task_id=14, execution_time=2, weight=1, required_r1=1, required_r2=4, period=3)
        task15 = tt(task_id=15, execution_time=2, weight=1, required_r1=1, required_r2=4, period=5)
        task16 = Task(task_id=16, execution_time=8, weight=1, required_r1=1, required_r2=2)
        task17 = Task(task_id=17, execution_time=5, weight=1, required_r1=1, required_r2=2)

        task18 = t_4(task_id=18, execution_time=10, required_r1=1, required_r2=1,dependencies=[])
        task19 = t_4(task_id=19, execution_time=8,  required_r1=1, required_r2=2,dependencies=[18])
        task20 = t_4(task_id=20, execution_time=12,  required_r1=1, required_r2=2,dependencies=[18])
        task21 = t_4(task_id=21, execution_time=12,  required_r1=1, required_r2=2,dependencies=[19,20])
        subsystem4.add_task(task18)
        subsystem4.add_task(task19)
        subsystem4.add_task(task20)
        subsystem4.add_task(task21)
        subsystem1.add_task(task1)
        subsystem1.add_task(task2)
        subsystem1.add_task(task3)
        subsystem1.add_task(task4)
        subsystem1.add_task(task5)
        subsystem1.add_task(task6)
        subsystem1.add_task(task7)
        subsystem1.add_task(task8)
        subsystem1.add_task(task9)
        
        subsystem2.add_task(task16)
        subsystem2.add_task(task17)
        
        subsystem3.add_task(task10)
        subsystem3.add_task(task11)
        subsystem3.add_task(task12)
        subsystem3.add_task(task13)
        subsystem3.add_task(task14)
        subsystem3.add_task(task15)

        # subsystem1.start()
        # waiting_queue_thread = threading.Thread(target=subsystem1.manage_waiting_queue)
        # waiting_queue_thread.daemon = True
        # waiting_queue_thread.start()
        
        # subsystem2.start()
        # subsystem3.start()
        
        # total_cores = len(subsystem1.cores) + len(subsystem2.cores) + len(subsystem3.core)
        # total_cores = 3 + 2 + 1
    
        # # 5) Create one barrier for *all* scheduling threads
        # barrier = threading.Barrier(total_cores + 1) # 1 more for the logger.

        # # 6) Pass this barrier to each subsystem (which will pass it to its cores)
        # subsystem1.set_sync_barrier(barrier)
        # subsystem2.set_sync_barrier(barrier)
        # subsystem3.set_sync_barrier(barrier)

        # # 7) Start each subsystem’s cores
        # subsystem1.start()
        # subsystem2.start()
        # subsystem3.start()

        # # If Subsystem1 has a separate waiting queue thread, you can start that too:
        # waiting_queue_thread = threading.Thread(target=subsystem1.manage_waiting_queue)
        # waiting_queue_thread.daemon = True
        # waiting_queue_thread.start()

        # # 8. Create and start the logger thread
        # logger_thread = LoggerThread(barrier, [subsystem1, subsystem2, subsystem3])
        # logger_thread.start()
        
        total_cores = 3 + 2 + 1 + 2
    
        # 5) Create one barrier for *all* scheduling threads
        barrier = threading.Barrier(total_cores + 1) # 1 more for the logger.

        # 6) Pass this barrier to each subsystem (which will pass it to its cores)
        subsystem1.set_sync_barrier(barrier)
        subsystem2.set_sync_barrier(barrier)
        subsystem3.set_sync_barrier(barrier)
        subsystem4.set_sync_barrier(barrier)

        # 7) Start each subsystem’s cores
        subsystem1.start()
        subsystem2.start()
        subsystem3.start()
        subsystem4.start()

        # If Subsystem1 has a separate waiting queue thread, you can start that too:
        waiting_queue_thread = threading.Thread(target=subsystem1.manage_waiting_queue)
        waiting_queue_thread.daemon = True
        waiting_queue_thread.start()

        # 8. Create and start the logger thread
        logger_thread = LoggerThread(barrier, [subsystem1, subsystem2, subsystem3, subsystem4])
        logger_thread.start()
        
        
        ##//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        threading.Thread(target=self.monitorer_name, args=(subsystem1.ready_queues[0], "set_ready_queue_subsys1_1")).start()
        threading.Thread(target=self.monitorer_name, args=(subsystem1.ready_queues[1], "set_ready_queue_subsys1_2")).start()
        threading.Thread(target=self.monitorer_name, args=(subsystem1.ready_queues[2], "set_ready_queue_subsys1_3")).start()
        threading.Thread(target=self.monitorer_tuple, args=(subsystem2.ready_queue, "set_ready_queue_subsys2")).start()
        threading.Thread(target=self.monitorer_tuple, args=(subsystem3.waiting_queue, "set_ready_queue_subsys3")).start() 
        threading.Thread(target=self.monitorer_name, args=(subsystem4.ready_queue, "set_ready_queue_subsys4")).start() 
        
        
        time.sleep(25)
        subsystem1.stop()
        subsystem2.stop()
        subsystem3.stop()
                   



    def collect_input(self):
        subsystem_tasks = [[] for _ in range(4)]  # Create a list to store tasks for each subsystem
        subsys_resource = []

        print("Enter resources for each subsystem:")
        for i in range(4):
            line = input()
            subsys_resource.append(list(map(int, line.split())))

        print("Subsystem Resources:", subsys_resource)

        print("\nEnter tasks for each subsystem (end input for a subsystem with $):")
        for i in range(4):
            print(f"\nSubsystem {i + 1}:")
            tasks = []
            while True:
                line = input()
                if line == "$":  # Separator for subsystems
                    break

                task_details = line.split()
                task_name = task_details[0]
                task_len = int(task_details[1])
                resource1 = int(task_details[2])
                resource2 = int(task_details[3])
                enter_time = int(task_details[4])

                if i == 0:  # Subsystem 1
                    dest_cpu = int(task_details[5])
                    task = {
                        "name": task_name,
                        "len": task_len,
                        "resource1": resource1,
                        "resource2": resource2,
                        "enter_time": enter_time,
                        "dest_cpu": dest_cpu,
                    }
                elif i == 1:  # Subsystem 2
                    task = {
                        "name": task_name,
                        "len": task_len,
                        "resource1": resource1,
                        "resource2": resource2,
                        "enter_time": enter_time,
                    }
                elif i == 2:  # Subsystem 3
                    period = int(task_details[5])
                    num_repeats = int(task_details[6])
                    task = {
                        "name": task_name,
                        "len": task_len,
                        "resource1": resource1,
                        "resource2": resource2,
                        "enter_time": enter_time,
                        "period": period,
                        "num_repeats": num_repeats,
                    }
                elif i == 3:  # Subsystem 4
                    pre_requisite = task_details[5]
                    task = {
                        "name": task_name,
                        "len": task_len,
                        "resource1": resource1,
                        "resource2": resource2,
                        "enter_time": enter_time,
                        "pre_requisite": pre_requisite,
                    }

                tasks.append(task)

            subsystem_tasks[i] = tasks

        return subsys_resource, subsystem_tasks
            

    # def additional_task(self, hi):
    #     print(f"Additional thread running with argument: {hi}")
    #     # Perform any additional work in this thread
    #     for i in range(5):
    #         time.sleep(1)
    #         print(f"Additional task iteration {i}: {hi}")