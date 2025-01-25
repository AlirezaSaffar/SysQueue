import threading
import time
from queue import Queue
from task import Task
from core1 import ProcessorCore

class Subsystem1:
    def __init__(self, r1_count, r2_count, time_slice):
        self.r1 = r1_count  
        self.r2 = r2_count 
        self.time_slice = time_slice 
        self.ready_queues = [Queue() for _ in range(3)]  
        self.waiting_queue = Queue()  
        self.cores = [ProcessorCore(i, self.ready_queues[i], self, time_slice) for i in range(3)]  
        self.num = 0

    def add_task(self, task):
        core_id = self.num % 3
        self.num += 1
        
        if 0 <= core_id < len(self.ready_queues):
            self.ready_queues[core_id].put(task)
            print(f"Task {task.task_id} added to Core {core_id} Ready Queue")
        else:
            print(f"Invalid Core ID: {core_id}")
    
    

    def add_to_waiting_queue(self, task):
       
        self.waiting_queue.put(task)
        print(f"Task {task.task_id} added to Waiting Queue")

    def check_resources(self, task):
       
        if self.r1 >= task.required_r1 and self.r2 >= task.required_r2:
            return True
        return False

    def allocate_resources(self, task):
       
        self.r1 -= task.required_r1
        self.r2 -= task.required_r2

    def release_resources(self, task):
      
        self.r1 += task.required_r1
        self.r2 += task.required_r2

    def start(self):
        for core in self.cores:
            core.start()

    def stop(self):
        for core in self.cores:
            core.running = False
        for core in self.cores:
            core.join()

    def check_waiting_queue(self):
        
        while not self.waiting_queue.empty():
            task = self.waiting_queue.queue[0]  
            if self.check_resources(task):  
                print(f"Task {task.task_id} moved from Waiting Queue to Ready Queue")
                self.waiting_queue.get() 
                core_id = self.num % 3
                self.ready_queues[core_id].put(task) 
                task.state = "Ready" 
            else:
                break  

    def manage_waiting_queue(self):
       
        while True:
            self.check_waiting_queue()  
            time.sleep(2)  