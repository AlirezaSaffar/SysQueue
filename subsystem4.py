import threading
import time
import random
from queue import Queue
from ss4task import Task
from core4 import ProcessorCoreFCFS


class Subsystem4:
    def __init__(self, r1_count, r2_count):
        self.r1 = r1_count 
        self.r2 = r2_count  
        self.ready_queue = Queue() 
        self.waiting_queue = Queue()  
        self.completed_tasks = set() 
        self.lock = threading.Lock() 
        self.core1 = ProcessorCoreFCFS(1, self)  
        self.core2 = ProcessorCoreFCFS(2, self)  
        self.running = True  
    def add_task(self, task):
       
        with self.lock:
            if all(dep in self.completed_tasks for dep in task.dependencies): 
                if self.check_resources(task): 
                    self.allocate_resources(task)
                    self.ready_queue.put(task)  
                    print(f"Task {task.task_id} added to Ready Queue.")
                else:
                    self.waiting_queue.put(task) 
                    print(f"Task {task.task_id} added to Waiting Queue due to insufficient resources.")
            else:
                self.waiting_queue.put(task) 
                print(f"Task {task.task_id} added to Waiting Queue due to unmet dependencies.")

    def check_resources(self, task):
       
        return self.r1 >= task.required_r1 and self.r2 >= task.required_r2

    def allocate_resources(self, task):
        
        self.r1 -= task.required_r1
        self.r2 -= task.required_r2
        print(f"Resources allocated for Task {task.task_id}: R1={task.required_r1}, R2={task.required_r2}")

    def release_resources(self, task):
        
        self.r1 += task.required_r1
        self.r2 += task.required_r2
        print(f"Resources released for Task {task.task_id}: R1={task.required_r1}, R2={task.required_r2}")

    def process_waiting_queue(self):
        
        with self.lock:
            for _ in range(self.waiting_queue.qsize()):
                task = self.waiting_queue.get()
                if all(dep in self.completed_tasks for dep in task.dependencies) and self.check_resources(task):
                    self.allocate_resources(task)
                    self.ready_queue.put(task)
                    print(f"Task {task.task_id} moved from Waiting Queue to Ready Queue.")
                else:
                    self.waiting_queue.put(task)  

    def start(self):
        
        self.core1.start()
        self.core2.start()

    def stop(self):
       
        self.running = False
        self.core1.running = False
        self.core2.running = False
        self.core1.join()
        self.core2.join()

