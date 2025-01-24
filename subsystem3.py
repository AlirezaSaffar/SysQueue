import threading
import time
from queue import PriorityQueue, Queue
from core3 import ProcessorCoreRateMonotonic

class Subsystem3:
    def __init__(self, r1_count, r2_count):
        self.r1 = r1_count  
        self.r2 = r2_count  
        self.ready_queue = PriorityQueue()  
        self.waiting_queue = Queue() 
        self.lock = threading.Lock() 
        self.core = ProcessorCoreRateMonotonic(self)  
        self.running = True  

    def add_task(self, task):
       
        with self.lock:
            if self.check_resources(task): 
                self.allocate_resources(task)  
                self.ready_queue.put((task.period, task))
                print(f"Task {task.task_id} added to Ready Queue with period {task.period}")
            else:
                self.waiting_queue.put(task)  
                print(f"Task {task.task_id} added to Waiting Queue due to insufficient resources.")

    def check_resources(self, task):
       
        return self.r1 >= task.required_r1 and self.r2 >= task.required_r2

    def allocate_resources(self, task):
       
        self.r1 -= task.required_r1
        self.r2 -= task.required_r2

    def release_resources(self, task):
      
        self.r1 += task.required_r1
        self.r2 += task.required_r2

    def process_waiting_queue(self):
        
        with self.lock:
            for _ in range(self.waiting_queue.qsize()):
                task = self.waiting_queue.get()
                if self.check_resources(task):
                    self.allocate_resources(task)
                    self.ready_queue.put((task.period, task))
                    print(f"Task {task.task_id} moved from Waiting Queue to Ready Queue.")
                else:
                    self.waiting_queue.put(task)  

    def start(self):
       
        self.core.start()

    def stop(self):
        
        self.running = False
        self.core.running = False
        self.core.join()


